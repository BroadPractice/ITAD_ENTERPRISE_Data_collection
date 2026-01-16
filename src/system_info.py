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
import psutil
import platform
import socket
# Additional imports will be added when dependencies are installed


class SystemInfoCollector:  # Main class to collect system information
    
    def __init__(self): 
        """Initialize the system information collector."""
        self.os_info = platform.system()
        self.hostname = socket.gethostname()
    
    def get_cpu_info(self): # Implemented function to get CPU info
        self.gpu_info = platform.processor()
        return self.gpu_info
    
    def get_gpu_info(self): # Implemented function to get GPU info
        self.gpu_info = platform.machine()
        return self.gpu_info
        
    
    def get_ram_info(self): # Implemented function to get RAM info
        self.ram_info = psutil.virtual_memory()
        return self.ram_info
    
    def get_storage_info(self): # Implemented function to get storage info
        self.storage_info = psutil.disk_partitions()
        return self.storage_info
        
    # def get_network_info(self): # Unneccessary function
    #     """
    #     TODO: Retrieve network information
    #     Returns: dict with network adapters, IP addresses, MAC addresses
    #     """
    #     pass
    
    def get_system_info(self): # Implemented function to get general system info
        self.general_info = platform.uname()
        return self.general_info
    
    def collect_all(self):  # Implemented function to call all info functions
        full_info = {}
        full_info["cpu"] = self.get_cpu_info()
        full_info["gpu"] = self.get_gpu_info()
        full_info["ram"] = self.get_ram_info()
        full_info["storage"] = self.get_storage_info()
        full_info["network"] = self.get_network_info()
        full_info["system"] = self.get_system_info()
        return full_info