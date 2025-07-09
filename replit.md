# GhostMedic AI Commander Bot

## Overview

GhostMedic is a sophisticated AI-powered bot system designed for PTM (Player Team Member) healing and automated corpsmen bot deployment across multiple platforms. The system provides intelligent decision-making capabilities, automated healing functions, and comprehensive monitoring across Discord, Slack, Telegram, and other platforms.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Architecture Pattern
The system follows a modular, component-based architecture with clear separation of concerns:

- **Core Engine**: Central `GhostMedicCore` class that orchestrates all system components
- **Configuration Management**: JSON-based configuration system with defaults and environment variable support
- **Logging System**: Centralized logging with rotation and level controls
- **Utility Layer**: Common helper functions and decorators for retry logic, rate limiting, and system utilities

### Key Design Decisions

1. **Modular Component Design**: Each major functionality (AI, healing, deployment, monitoring) is encapsulated in separate classes
2. **Asynchronous Processing**: Uses asyncio for concurrent operations and threading for worker management
3. **Configuration-Driven**: All system behavior is configurable through JSON files and environment variables
4. **Comprehensive Error Handling**: Retry mechanisms and rate limiting built into core operations

## Key Components

### 1. Core System (`ghostmedic/core.py`)
- **GhostMedicCore**: Main orchestrator class that manages all subsystems
- **AIEngine**: Handles AI model integration and intelligent decision making
- **HealingSystem**: Manages PTM healing operations and intervals
- **DeploymentManager**: Handles corpsmen bot deployment across platforms
- **MonitoringSystem**: Provides system health monitoring and diagnostics

### 2. Configuration Management (`config.py`)
- **Config Class**: Centralized configuration management with defaults
- **Environment Integration**: Support for environment variables and file-based config
- **Validation**: Configuration validation and error handling
- **Categories**: System, logging, AI, bot, platform, security, and monitoring configurations

### 3. Logging System (`ghostmedic/logger.py`)
- **Centralized Setup**: Single function to configure all logging
- **File Rotation**: Automatic log file rotation with size and count limits
- **Multiple Handlers**: Console and file logging support
- **Configurable Levels**: Support for different log levels and formats

### 4. Utilities (`utils.py`)
- **System Utilities**: Directory creation, file hashing, timestamp generation
- **Decorators**: Retry logic, rate limiting, and timing decorators
- **Helper Functions**: Common operations used across the system

## Data Flow

### 1. System Initialization
1. Configuration loaded from file or defaults
2. Logging system initialized
3. Core components instantiated
4. AI engine and platform connections established

### 2. Main Operation Loop
1. Core system starts worker threads
2. Healing system monitors PTM status
3. AI engine processes decisions
4. Deployment manager handles bot operations
5. Monitoring system tracks performance

### 3. Configuration Updates
- Runtime configuration changes supported
- Automatic reloading of configuration files
- Environment variable override support

## External Dependencies

### AI Integration
- **OpenAI API**: Primary AI model integration (GPT-3.5-turbo default)
- **Configurable Models**: Support for different AI models and providers
- **API Key Management**: Secure API key handling through environment variables

### Platform Integrations
- **Discord**: Bot deployment and messaging
- **Slack**: Workspace integration
- **Telegram**: Bot API integration
- **Extensible**: Architecture supports additional platforms

### System Dependencies
- **Python 3.x**: Core runtime environment
- **Asyncio**: Asynchronous operation support
- **Threading**: Multi-worker support
- **JSON**: Configuration file format
- **Logging**: Built-in Python logging system

## Deployment Strategy

### Development Mode
- **Interactive CLI**: Command-line interface for development and testing
- **Debug Configuration**: Verbose logging and debug mode support
- **Test Framework**: Comprehensive unit tests for all components

### Production Deployment
- **Daemon Mode**: Background service operation
- **Configuration Management**: External configuration file support
- **Monitoring**: Built-in health monitoring and diagnostics
- **Logging**: Production-ready logging with rotation

### Scaling Considerations
- **Worker Threads**: Configurable number of worker threads
- **Rate Limiting**: Built-in API rate limiting
- **Timeout Management**: Configurable timeout values
- **Resource Monitoring**: System resource usage tracking

### Security Features
- **API Key Protection**: Secure handling of API keys and tokens
- **Rate Limiting**: Protection against API abuse
- **Configuration Validation**: Input validation and sanitization
- **Logging Security**: Sensitive data filtering in logs

## Development Notes

### Testing Strategy
- **Unit Tests**: Comprehensive test coverage for all components
- **Mock Integration**: External service mocking for testing
- **Configuration Testing**: Test configuration loading and validation
- **Error Handling**: Test error conditions and recovery

### Code Organization
- **Package Structure**: Clear separation of concerns in package layout
- **Import Management**: Clean import structure and dependency management
- **Documentation**: Comprehensive docstrings and type hints
- **Standards**: Consistent coding style and patterns

### Extension Points
- **Plugin Architecture**: Support for additional AI engines
- **Platform Extensions**: Easy addition of new platforms
- **Custom Healing Logic**: Configurable healing algorithms
- **Monitoring Extensions**: Custom monitoring and alerting