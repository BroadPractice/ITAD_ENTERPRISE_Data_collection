"""
json_handler.py

PURPOSE:
    This module handles JSON serialization and file operations for system data.
    It converts collected system information to JSON format and manages file I/O.

RESPONSIBILITIES:
    - Convert system information dictionary to JSON format
    - Write JSON data to files
    - Read JSON data from files
    - Validate JSON structure
    - Handle custom serialization for non-standard types (datetime, etc.)
    - Manage JSON file naming and organization

DEPENDENCIES:
    - json (built-in)
    - datetime (built-in for timestamps)

EXAMPLE:
    handler = JSONHandler()
    handler.save_system_info(system_data, "output.json")
    data = handler.load_system_info("output.json")
"""

import json
from datetime import datetime
from pathlib import Path


class JSONHandler:
    """
    Handles JSON serialization and file operations for system information.
    """
    
    def __init__(self, data_dir="../data"):
        """
        Initialize JSON handler with data directory.
        
        Args:
            data_dir (str): Path to directory where JSON files will be stored
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def save_system_info(self, system_data, filename=None):
        """
        Save system information to a JSON file.

        TODO: Implement JSON serialization with timestamp
        
        Args:
            system_data (dict): System information dictionary to save
            filename (str, optional): Custom filename. If None, use timestamp.
        
        Returns:
            str: Path to saved file
        """
        self.system_data = self.append_timestamp(system_data)
        self.system_data = json.loads(json.dumps(self.system_data, default=str))
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"system_info_{timestamp}.json"
        else:
            filename = f"{filename}.json"

        return str(self.data_dir / filename)
    
    def load_system_info(self, filename):
        """
        Load system information from a JSON file.
        
        TODO: Implement JSON file reading and validation
        
        Args:
            filename (str): Name of the JSON file to load
        
        Returns:
            dict: Loaded system information
        
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file is not valid JSON
        """
        file_name = self.data_dir / filename
        with open(file_name, 'r') as file:
            data = json.load(file)

        return data
    
    def append_timestamp(self, data):
        """
        Add timestamp to system data.
        
        TODO: Implement timestamp addition for tracking when data was collected
        
        Args:
            data (dict): System information dictionary
        
        Returns:
            dict: Data with added timestamp
        """
        time_stamp = datetime.now().isoformat()
        data['timestamp'] = time_stamp
        return data
    
    def validate_json_structure(self, data):
        """
        Validate that the system data has the expected JSON structure.        
        Args:
            data (dict): Data to validate
        
        Returns:
            bool: True if valid, False otherwise
        """
        key_expected = {'cpu', 'memory', 'disk', 'timestamp'}
        if not isinstance(data, dict):
            return False
        else:
            return key_expected.issubset(data.keys())

    
    def custom_json_encoder(self):
        """
        TODO: Create custom JSON encoder for non-standard types
        (e.g., datetime, bytes, custom objects)
        
        Returns:
            json.JSONEncoder: Custom encoder class
        """
        class CustomEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, datetime):
                    return obj.isoformat()
                return super().default(obj)
        
        return CustomEncoder
