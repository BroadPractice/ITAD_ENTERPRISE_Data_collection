"""
system_info.py

PURPOSE:
    This module handles the collection of system information from the host machine.
    It gathers data about CPU, GPU, RAM, storage, and other hardware specifications.

RESPONSIBILITIES:
    - Detect and retrieve CPU information (model, cores, threads, frequency)
    - Detect and retrieve GPU information (NVIDIA, AMD, Intel integrated)
    - Detect and retrieve RAM information (total, available, used)
    - Detect and retrieve HDD/SSD information (drives, capacity, free space, type)
    - Detect OS and system information
    - Detect network information
    - Handle platform-specific differences (Windows, Linux, macOS)

DEPENDENCIES TO ADD:
    - psutil: For CPU, RAM, and disk information
    - GPUtil or gpu-stat: For GPU information
    - wmi (Windows) or subprocess calls for Windows-specific hardware info

EXAMPLE OUTPUT:
    {
        "cpu": {"model": "Intel Core i7", "cores": 8, "threads": 16, ...},
        "gpu": {"model": "NVIDIA RTX 3080", "memory": 10GB, ...},
        "ram": {"total": 32GB, "available": 16GB, ...},
        "storage": [{"drive": "C:", "capacity": 500GB, "free": 250GB, "type": "SSD"}],
        ...
    }
"""

import platform
import socket
# Additional imports will be added when dependencies are installed


class SystemInfoCollector:
    """
    Collects comprehensive system information from the host machine.
    
    TODO: Implement methods for each hardware category
    """
    
    def __init__(self):
        """Initialize the system information collector."""
        self.os_info = platform.system()
        self.hostname = socket.gethostname()
    
    def get_cpu_info(self):
        """
        TODO: Retrieve CPU information
        Returns: dict with CPU model, cores, threads, frequency, etc.
        """
        pass
    
    def get_gpu_info(self):
        """
        TODO: Retrieve GPU information
        Returns: dict or list of dicts with GPU models, memory, etc.
        """
        pass
    
    def get_ram_info(self):
        """
        TODO: Retrieve RAM information
        Returns: dict with total, available, used RAM
        """
        pass
    
    def get_storage_info(self):
        """
        TODO: Retrieve storage information
        Returns: list of dicts with drive info (capacity, free space, type)
        """
        pass
    
    def get_network_info(self):
        """
        TODO: Retrieve network information
        Returns: dict with network adapters, IP addresses, MAC addresses
        """
        pass
    
    def get_system_info(self):
        """
        TODO: Retrieve general system information
        Returns: dict with OS, hostname, uptime, etc.
        """
        pass
    
    def collect_all(self):
        """
        Collect all system information and return as a unified dictionary.
        
        TODO: Implement to call all get_* methods and combine results
        Returns: dict with complete system information
        """
        pass
