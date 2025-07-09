"""
Logging configuration for GhostMedic AI Commander Bot

Centralized logging setup and configuration.
"""

import logging
import logging.handlers
import os
import sys
from typing import Optional
from datetime import datetime


def setup_logging(
    level: int = logging.INFO,
    log_file: Optional[str] = None,
    log_format: Optional[str] = None,
    max_bytes: int = 10 * 1024 * 1024,  # 10MB
    backup_count: int = 5
) -> logging.Logger:
    """
    Set up logging configuration for GhostMedic.
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Path to log file (optional)
        log_format: Custom log format (optional)
        max_bytes: Maximum log file size before rotation
        backup_count: Number of backup log files to keep
    
    Returns:
        Configured logger instance
    """
    
    # Default log format
    if log_format is None:
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # Create formatter
    formatter = logging.Formatter(log_format)
    
    # Get root logger
    logger = logging.getLogger()
    logger.setLevel(level)
    
    # Clear any existing handlers
    logger.handlers.clear()
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        # Ensure log directory exists
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        
        # Rotating file handler
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    # Set up specific loggers
    setup_component_loggers(level)
    
    logger.info("Logging system initialized")
    return logger


def setup_component_loggers(level: int):
    """Set up specific component loggers."""
    
    # GhostMedic components
    components = [
        'ghostmedic.core',
        'ghostmedic.logger',
        'config',
        'utils'
    ]
    
    for component in components:
        component_logger = logging.getLogger(component)
        component_logger.setLevel(level)
        # Don't propagate to avoid duplicate messages
        component_logger.propagate = True


def get_logger(name: str) -> logging.Logger:
    """Get a logger for a specific component."""
    return logging.getLogger(name)


class GhostMedicLogger:
    """Custom logger wrapper for GhostMedic components."""
    
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.component = name.split('.')[-1]
    
    def debug(self, message: str, **kwargs):
        """Log debug message."""
        self.logger.debug(f"[{self.component}] {message}", **kwargs)
    
    def info(self, message: str, **kwargs):
        """Log info message."""
        self.logger.info(f"[{self.component}] {message}", **kwargs)
    
    def warning(self, message: str, **kwargs):
        """Log warning message."""
        self.logger.warning(f"[{self.component}] {message}", **kwargs)
    
    def error(self, message: str, **kwargs):
        """Log error message."""
        self.logger.error(f"[{self.component}] {message}", **kwargs)
    
    def critical(self, message: str, **kwargs):
        """Log critical message."""
        self.logger.critical(f"[{self.component}] {message}", **kwargs)
    
    def exception(self, message: str, **kwargs):
        """Log exception with traceback."""
        self.logger.exception(f"[{self.component}] {message}", **kwargs)


class LogContext:
    """Context manager for structured logging."""
    
    def __init__(self, logger: logging.Logger, operation: str, **context):
        self.logger = logger
        self.operation = operation
        self.context = context
        self.start_time = None
    
    def __enter__(self):
        self.start_time = datetime.now()
        context_str = ', '.join(f"{k}={v}" for k, v in self.context.items())
        self.logger.info(f"Starting {self.operation} - {context_str}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = datetime.now() - self.start_time
        
        if exc_type is None:
            self.logger.info(f"Completed {self.operation} in {duration}")
        else:
            self.logger.error(f"Failed {self.operation} after {duration}: {exc_val}")
    
    def update_context(self, **kwargs):
        """Update context information."""
        self.context.update(kwargs)


def log_function_call(logger: logging.Logger):
    """Decorator to log function calls."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            logger.debug(f"Calling {func_name} with args={args}, kwargs={kwargs}")
            
            try:
                result = func(*args, **kwargs)
                logger.debug(f"Function {func_name} completed successfully")
                return result
            except Exception as e:
                logger.error(f"Function {func_name} failed: {e}")
                raise
        
        return wrapper
    return decorator


def configure_third_party_loggers():
    """Configure third-party library loggers."""
    # Reduce noise from third-party libraries
    noisy_loggers = [
        'urllib3.connectionpool',
        'requests.packages.urllib3.connectionpool',
        'asyncio',
        'aiohttp.access'
    ]
    
    for logger_name in noisy_loggers:
        logging.getLogger(logger_name).setLevel(logging.WARNING)


# Initialize third-party logger configuration
configure_third_party_loggers()
