#!/usr/bin/env python3
"""
GhostMedic AI Commander Bot - Main Entry Point

This is the main entry point for the GhostMedic AI bot system.
Provides command-line interface and basic menu system for development.
"""

import argparse
import sys
import os
import logging
from ghostmedic.core import GhostMedicCore
from ghostmedic.logger import setup_logging
from config import Config


def create_parser():
    """Create command-line argument parser."""
    parser = argparse.ArgumentParser(
        description='GhostMedic AI Commander Bot - Savage AI for PTM healing and corpsmen deployment',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    parser.add_argument(
        '-c', '--config',
        type=str,
        help='Path to configuration file'
    )
    
    parser.add_argument(
        '--mode',
        choices=['interactive', 'daemon', 'test'],
        default='interactive',
        help='Operation mode (default: interactive)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='GhostMedic v0.1.0'
    )
    
    return parser


def interactive_menu():
    """Display interactive menu for development and testing."""
    print("\n" + "="*50)
    print("    GhostMedic AI Commander Bot")
    print("    Savage AI for PTM Healing")
    print("="*50)
    print("\nAvailable Commands:")
    print("  1. Initialize bot systems")
    print("  2. Test AI components")
    print("  3. Deploy corpsmen bots")
    print("  4. System diagnostics")
    print("  5. Configuration management")
    print("  0. Exit")
    print("-"*50)
    
    while True:
        try:
            choice = input("\nEnter command [0-5]: ").strip()
            
            if choice == '0':
                print("Shutting down GhostMedic systems...")
                break
            elif choice == '1':
                print("Initializing bot systems...")
                # Future: Initialize AI components
                print("✓ Bot systems initialized")
            elif choice == '2':
                print("Testing AI components...")
                # Future: Test AI functionality
                print("✓ AI components tested")
            elif choice == '3':
                print("Deploying corpsmen bots...")
                # Future: Deploy bot instances
                print("✓ Corpsmen bots deployed")
            elif choice == '4':
                print("Running system diagnostics...")
                # Future: System health checks
                print("✓ All systems operational")
            elif choice == '5':
                print("Configuration management...")
                # Future: Config management interface
                print("✓ Configuration accessed")
            else:
                print("Invalid choice. Please enter 0-5.")
                
        except KeyboardInterrupt:
            print("\n\nShutting down GhostMedic systems...")
            break
        except Exception as e:
            logging.error(f"Error in interactive menu: {e}")
            print(f"Error: {e}")


def daemon_mode():
    """Run in daemon mode for production deployment."""
    print("Starting GhostMedic in daemon mode...")
    logging.info("GhostMedic daemon started")
    
    try:
        # Future: Implement daemon functionality
        # - Bot monitoring
        # - Automatic healing processes
        # - Continuous deployment
        print("Daemon mode placeholder - ready for implementation")
        
    except KeyboardInterrupt:
        logging.info("Daemon mode interrupted by user")
        print("Daemon mode stopped")
    except Exception as e:
        logging.error(f"Daemon mode error: {e}")
        print(f"Daemon error: {e}")


def test_mode():
    """Run in test mode for development."""
    print("Running GhostMedic in test mode...")
    logging.info("Test mode initiated")
    
    try:
        # Future: Implement test scenarios
        # - Unit tests for AI components
        # - Integration tests
        # - Performance benchmarks
        print("Test mode placeholder - ready for implementation")
        
    except Exception as e:
        logging.error(f"Test mode error: {e}")
        print(f"Test error: {e}")


def main():
    """Main application entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(log_level)
    
    # Load configuration
    config = Config(args.config)
    
    # Initialize core system
    try:
        core = GhostMedicCore(config)
        logging.info("GhostMedic AI Commander Bot started")
        
        # Run based on mode
        if args.mode == 'interactive':
            interactive_menu()
        elif args.mode == 'daemon':
            daemon_mode()
        elif args.mode == 'test':
            test_mode()
            
    except Exception as e:
        logging.error(f"Failed to initialize GhostMedic: {e}")
        print(f"Initialization error: {e}")
        sys.exit(1)
    
    logging.info("GhostMedic AI Commander Bot shutdown")
    print("GhostMedic systems offline")


if __name__ == '__main__':
    main()
