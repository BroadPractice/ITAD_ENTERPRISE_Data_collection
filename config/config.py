"""
config.py

PURPOSE:
    This module handles configuration management for the application.
    It loads settings from configuration files and environment variables.

RESPONSIBILITIES:
    - Load configuration from config files (JSON, YAML, or INI)
    - Load configuration from environment variables
    - Provide default values
    - Validate configuration
    - Support different environments (dev, test, production)

CONFIGURATION ITEMS TO MANAGE:
    - Database connection string and type
    - Data directory path
    - Log level and log file path
    - Schedule settings (if implementing periodic collection)
    - API endpoints (if implementing web API)
    - Timeout values
    - Feature flags

DEPENDENCIES:
    - json (built-in)
    - os (built-in) for environment variables

EXAMPLE CONFIG FILE (config/settings.json):
    {
        "database": {
            "type": "sqlite",
            "connection_string": "../data/systems.db"
        },
        "logging": {
            "level": "INFO",
            "log_file": "../logs/application.log"
        },
        "data": {
            "directory": "../data",
            "retention_days": 365
        }
    }
"""

import json
import os
from pathlib import Path


class Config:
    """
    Manages application configuration from files and environment variables.
    """
    
    # Default configuration values
    DEFAULTS = {
        "database": {
            "type": "sqlite",
            "connection_string": "data/systems.db"
        },
        "logging": {
            "level": "INFO",
            "log_file": "logs/application.log"
        },
        "data": {
            "directory": "data",
            "retention_days": 365
        }
    }
    
    def __init__(self, config_file=None):
        """
        Initialize configuration manager.
        
        Args:
            config_file (str, optional): Path to config file. If None, uses defaults.
        """
        self.config = self.DEFAULTS.copy()
        self.config_file = config_file
        
        if config_file:
            self.load_from_file(config_file)
        
        self.load_from_environment()
    
    def load_from_file(self, config_file):
        """
        TODO: Load configuration from JSON file
        
        Args:
            config_file (str): Path to configuration file
        
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file is not valid JSON
        """
        pass
    
    def load_from_environment(self):
        """
        TODO: Load configuration from environment variables
        
        Environment variables should be prefixed with ITAD_
        Example: ITAD_DATABASE_TYPE, ITAD_LOG_LEVEL
        """
        pass
    
    def get(self, key, default=None):
        """
        Get a configuration value by key (supports nested keys with dots).
        
        Args:
            key (str): Configuration key (e.g., "database.type")
            default: Default value if key not found
        
        Returns:
            Configuration value or default
        """
        # TODO: Implement nested key lookup (e.g., "database.type")
        pass
    
    def validate(self):
        """
        TODO: Validate that required configuration values are present
        
        Returns:
            bool: True if valid
        
        Raises:
            ValueError: If configuration is invalid
        """
        pass
    
    def to_dict(self):
        """
        Return configuration as dictionary.
        
        Returns:
            dict: Current configuration
        """
        return self.config
