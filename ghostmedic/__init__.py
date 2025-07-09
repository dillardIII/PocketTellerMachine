"""
GhostMedic AI Commander Bot Package

A savage AI system for PTM healing and corpsmen bot deployment.
"""

__version__ = '0.1.0'
__author__ = 'GhostMedic Team'
__description__ = 'Savage AI Commander Bot for PTM healing and corpsmen deployment'

from .core import GhostMedicCore
from .logger import setup_logging

__all__ = ['GhostMedicCore', 'setup_logging']
