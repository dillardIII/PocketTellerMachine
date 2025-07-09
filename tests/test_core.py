"""
Unit tests for GhostMedic core functionality
"""

import unittest
import tempfile
import os
import json
from unittest.mock import Mock, patch, MagicMock
import threading
import time

# Import modules to test
from config import Config
from ghostmedic.core import GhostMedicCore, AIEngine, HealingSystem, DeploymentManager, MonitoringSystem
from ghostmedic.logger import setup_logging
from utils import Timer, RateLimiter, retry_on_exception, format_bytes, format_duration


class TestConfig(unittest.TestCase):
    """Test configuration management."""
    
    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        self.config_file = os.path.join(self.temp_dir, 'test_config.json')
    
    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.config_file):
            os.remove(self.config_file)
        os.rmdir(self.temp_dir)
    
    def test_default_config(self):
        """Test default configuration loading."""
        config = Config()
        
        self.assertEqual(config.get('system.name'), 'GhostMedic AI Commander Bot')
        self.assertEqual(config.get('system.version'), '0.1.0')
        self.assertEqual(config.get('bot.corpsmen_count'), 3)
        self.assertIsInstance(config.get('bot.platforms'), list)
    
    def test_config_file_loading(self):
        """Test loading configuration from file."""
        test_config = {
            'system': {
                'name': 'Test GhostMedic',
                'debug': True
            },
            'bot': {
                'corpsmen_count': 5
            }
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(test_config, f)
        
        config = Config(self.config_file)
        
        self.assertEqual(config.get('system.name'), 'Test GhostMedic')
        self.assertEqual(config.get('system.debug'), True)
        self.assertEqual(config.get('bot.corpsmen_count'), 5)
        # Default values should still be present
        self.assertEqual(config.get('system.version'), '0.1.0')
    
    def test_config_get_set(self):
        """Test configuration get and set operations."""
        config = Config()
        
        # Test get with default
        self.assertEqual(config.get('nonexistent.key', 'default'), 'default')
        
        # Test set and get
        config.set('test.key', 'test_value')
        self.assertEqual(config.get('test.key'), 'test_value')
    
    def test_config_validation(self):
        """Test configuration validation."""
        config = Config()
        
        # Valid configuration should pass
        self.assertTrue(config.validate())
        
        # Invalid configuration should fail
        config.set('system.max_workers', -1)
        self.assertFalse(config.validate())


class TestUtils(unittest.TestCase):
    """Test utility functions."""
    
    def test_format_bytes(self):
        """Test byte formatting."""
        self.assertEqual(format_bytes(1024), '1.0 KB')
        self.assertEqual(format_bytes(1024**2), '1.0 MB')
        self.assertEqual(format_bytes(1024**3), '1.0 GB')
    
    def test_format_duration(self):
        """Test duration formatting."""
        self.assertEqual(format_duration(30), '30.0s')
        self.assertEqual(format_duration(90), '1.5m')
        self.assertEqual(format_duration(3600), '1.0h')
        self.assertEqual(format_duration(86400), '1.0d')
    
    def test_timer(self):
        """Test Timer context manager."""
        with Timer("Test operation") as timer:
            time.sleep(0.1)
        
        self.assertGreater(timer.elapsed, 0.1)
        self.assertLess(timer.elapsed, 0.2)
    
    def test_rate_limiter(self):
        """Test RateLimiter functionality."""
        limiter = RateLimiter(max_calls=2, time_window=1.0)
        
        # First two calls should be allowed
        self.assertTrue(limiter.is_allowed())
        self.assertTrue(limiter.is_allowed())
        
        # Third call should be denied
        self.assertFalse(limiter.is_allowed())
        
        # After time window, should be allowed again
        time.sleep(1.1)
        self.assertTrue(limiter.is_allowed())
    
    def test_retry_decorator(self):
        """Test retry decorator."""
        call_count = 0
        
        @retry_on_exception(max_retries=3, delay=0.1)
        def failing_function():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ValueError("Test error")
            return "success"
        
        result = failing_function()
        self.assertEqual(result, "success")
        self.assertEqual(call_count, 3)


class TestAIEngine(unittest.TestCase):
    """Test AI engine functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.config = Config()
        self.ai_engine = AIEngine(self.config)
    
    def test_ai_engine_initialization(self):
        """Test AI engine initialization."""
        self.assertTrue(self.ai_engine.is_ready)
        self.assertEqual(self.ai_engine.model, 'gpt-3.5-turbo')
    
    def test_process_command(self):
        """Test AI command processing."""
        response = self.ai_engine.process_command("test command")
        self.assertIn("AI response to: test command", response)
    
    def test_get_status(self):
        """Test AI engine status."""
        status = self.ai_engine.get_status()
        self.assertIn('ready', status)
        self.assertIn('model', status)
        self.assertIn('api_key_configured', status)


class TestHealingSystem(unittest.TestCase):
    """Test healing system functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.config = Config()
        self.healing_system = HealingSystem(self.config)
    
    def test_healing_system_initialization(self):
        """Test healing system initialization."""
        self.assertEqual(self.healing_system.healing_interval, 300)
        self.assertEqual(len(self.healing_system.active_healings), 0)
        self.assertFalse(self.healing_system.is_running)
    
    def test_healing_cycle(self):
        """Test healing cycle execution."""
        initial_count = len(self.healing_system.active_healings)
        self.healing_system._perform_healing_cycle()
        
        self.assertEqual(len(self.healing_system.active_healings), initial_count + 1)
        self.assertEqual(self.healing_system.active_healings[-1]['type'], 'ptm_healing')
    
    def test_get_status(self):
        """Test healing system status."""
        status = self.healing_system.get_status()
        self.assertIn('running', status)
        self.assertIn('active_healings', status)
        self.assertIn('healing_interval', status)


class TestDeploymentManager(unittest.TestCase):
    """Test deployment manager functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.config = Config()
        self.deployment_manager = DeploymentManager(self.config)
    
    def test_deployment_manager_initialization(self):
        """Test deployment manager initialization."""
        self.assertEqual(self.deployment_manager.corpsmen_count, 3)
        self.assertFalse(self.deployment_manager.auto_deploy)
        self.assertEqual(len(self.deployment_manager.deployed_bots), 0)
    
    def test_deploy_corpsman(self):
        """Test corpsman deployment."""
        initial_count = len(self.deployment_manager.deployed_bots)
        self.deployment_manager._deploy_corpsman('discord', 0)
        
        self.assertEqual(len(self.deployment_manager.deployed_bots), initial_count + 1)
        bot = self.deployment_manager.deployed_bots[-1]
        self.assertEqual(bot['platform'], 'discord')
        self.assertEqual(bot['index'], 0)
        self.assertEqual(bot['status'], 'active')
    
    def test_get_status(self):
        """Test deployment manager status."""
        status = self.deployment_manager.get_status()
        self.assertIn('running', status)
        self.assertIn('deployed_bots', status)
        self.assertIn('corpsmen_count', status)


class TestMonitoringSystem(unittest.TestCase):
    """Test monitoring system functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.config = Config()
        self.monitoring_system = MonitoringSystem(self.config)
    
    def test_monitoring_system_initialization(self):
        """Test monitoring system initialization."""
        self.assertIsNotNone(self.monitoring_system.start_time)
        self.assertIsInstance(self.monitoring_system.metrics, dict)
        self.assertFalse(self.monitoring_system.is_running)
    
    def test_get_uptime(self):
        """Test uptime calculation."""
        uptime = self.monitoring_system.get_uptime()
        self.assertIsInstance(uptime, str)
        self.assertGreater(len(uptime), 0)
    
    def test_get_status(self):
        """Test monitoring system status."""
        status = self.monitoring_system.get_status()
        self.assertIn('running', status)
        self.assertIn('uptime', status)
        self.assertIn('metrics', status)


class TestGhostMedicCore(unittest.TestCase):
    """Test GhostMedic core functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.config = Config()
        self.core = GhostMedicCore(self.config)
    
    def tearDown(self):
        """Clean up test environment."""
        if self.core.is_running:
            self.core.stop()
    
    def test_core_initialization(self):
        """Test core system initialization."""
        self.assertIsNotNone(self.core.ai_engine)
        self.assertIsNotNone(self.core.healing_system)
        self.assertIsNotNone(self.core.deployment_manager)
        self.assertIsNotNone(self.core.monitoring_system)
        self.assertFalse(self.core.is_running)
    
    def test_get_status(self):
        """Test core system status."""
        status = self.core.get_status()
        self.assertIn('running', status)
        self.assertIn('workers', status)
        self.assertIn('ai_engine', status)
        self.assertIn('healing_system', status)
        self.assertIn('deployment_manager', status)
        self.assertIn('monitoring_system', status)


class TestLogger(unittest.TestCase):
    """Test logging functionality."""
    
    def test_setup_logging(self):
        """Test logging setup."""
        logger = setup_logging()
        self.assertIsNotNone(logger)
        
        # Test logging levels
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")


if __name__ == '__main__':
    # Set up basic logging for tests
    setup_logging()
    
    # Run tests
    unittest.main(verbosity=2)
