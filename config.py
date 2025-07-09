"""
Configuration Management for GhostMedic AI Commander Bot

Handles configuration loading, validation, and management.
"""

import json
import os
import logging
from typing import Dict, Any, Optional


class Config:
    """Configuration manager for GhostMedic system."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize configuration with defaults and load from file if provided."""
        self.config_path = config_path or os.getenv('GHOSTMEDIC_CONFIG', 'config.json')
        self._config = self._load_defaults()
        
        # Load from file if exists
        if os.path.exists(self.config_path):
            self._load_from_file()
        else:
            logging.info(f"Config file not found: {self.config_path}, using defaults")
    
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default configuration values."""
        return {
            'system': {
                'name': 'GhostMedic AI Commander Bot',
                'version': '0.1.0',
                'debug': False,
                'max_workers': 4,
                'timeout': 30
            },
            'logging': {
                'level': 'INFO',
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                'file': 'ghostmedic.log',
                'max_size': 10485760,  # 10MB
                'backup_count': 5
            },
            'ai': {
                'model': 'gpt-3.5-turbo',
                'temperature': 0.7,
                'max_tokens': 1000,
                'api_key': os.getenv('OPENAI_API_KEY', ''),
                'base_url': 'https://api.openai.com/v1'
            },
            'bot': {
                'name': 'GhostMedic',
                'description': 'Savage AI Commander for PTM healing and corpsmen deployment',
                'platforms': ['discord', 'slack', 'telegram'],
                'auto_deploy': False,
                'healing_interval': 300,  # 5 minutes
                'corpsmen_count': 3
            },
            'security': {
                'encrypt_config': False,
                'api_rate_limit': 100,
                'max_retries': 3,
                'backoff_factor': 2
            }
        }
    
    def _load_from_file(self):
        """Load configuration from JSON file."""
        try:
            with open(self.config_path, 'r') as f:
                file_config = json.load(f)
                self._merge_config(file_config)
            logging.info(f"Configuration loaded from {self.config_path}")
        except Exception as e:
            logging.error(f"Failed to load config from {self.config_path}: {e}")
            raise
    
    def _merge_config(self, new_config: Dict[str, Any]):
        """Merge new configuration with existing config."""
        def merge_dict(base: Dict, update: Dict) -> Dict:
            for key, value in update.items():
                if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                    merge_dict(base[key], value)
                else:
                    base[key] = value
            return base
        
        merge_dict(self._config, new_config)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value using dot notation (e.g., 'system.name')."""
        keys = key.split('.')
        value = self._config
        
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, key: str, value: Any):
        """Set configuration value using dot notation."""
        keys = key.split('.')
        config = self._config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def save(self, path: Optional[str] = None):
        """Save current configuration to file."""
        save_path = path or self.config_path
        
        try:
            with open(save_path, 'w') as f:
                json.dump(self._config, f, indent=2)
            logging.info(f"Configuration saved to {save_path}")
        except Exception as e:
            logging.error(f"Failed to save config to {save_path}: {e}")
            raise
    
    def validate(self) -> bool:
        """Validate configuration values."""
        errors = []
        
        # Check required fields
        required_fields = [
            'system.name',
            'system.version',
            'logging.level',
            'bot.name'
        ]
        
        for field in required_fields:
            if not self.get(field):
                errors.append(f"Missing required field: {field}")
        
        # Validate specific values
        if self.get('system.max_workers', 0) <= 0:
            errors.append("system.max_workers must be positive")
        
        if self.get('system.timeout', 0) <= 0:
            errors.append("system.timeout must be positive")
        
        if self.get('logging.level') not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            errors.append("Invalid logging.level value")
        
        if errors:
            for error in errors:
                logging.error(f"Configuration validation error: {error}")
            return False
        
        return True
    
    def to_dict(self) -> Dict[str, Any]:
        """Return configuration as dictionary."""
        return self._config.copy()
    
    def __str__(self) -> str:
        """String representation of configuration."""
        return json.dumps(self._config, indent=2)
