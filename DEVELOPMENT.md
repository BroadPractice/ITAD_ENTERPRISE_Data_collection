# Development Roadmap

## Overview

This document outlines the next steps and development priorities for the ITAD Enterprise Data Collection system.

---

## Phase 1: Foundation (Priority: HIGH)

### 1.1 System Information Collection Implementation
**File**: `src/system_info.py`

- [ ] Implement `get_cpu_info()` method
  - Use `psutil.cpu_count()`, `psutil.cpu_freq()`, `cpuinfo` library
  - Detect CPU model name
  - Test on Windows, Linux, macOS

- [ ] Implement `get_gpu_info()` method
  - Detect NVIDIA GPUs (nvidia-ml-py)
  - Detect AMD GPUs (rocm-smi)
  - Detect Intel integrated graphics
  - Handle systems with no GPU gracefully

- [ ] Implement `get_ram_info()` method
  - Use `psutil.virtual_memory()`
  - Total, available, used RAM
  - Memory percentage

- [ ] Implement `get_storage_info()` method
  - Use `psutil.disk_partitions()` and `psutil.disk_usage()`
  - Detect drive type (SSD vs HDD) - **CHALLENGE: May need WMI on Windows**
  - Include total, used, and free space for each drive

- [ ] Implement `get_network_info()` method
  - Network adapters
  - IP addresses (IPv4, IPv6)
  - MAC addresses
  - Network speed/bandwidth info

- [ ] Implement `get_system_info()` method
  - OS name and version
  - Hostname
  - System uptime
  - Architecture (32-bit, 64-bit)

- [ ] Implement `collect_all()` method
  - Call all get_* methods
  - Combine into unified dictionary
  - Add metadata (collection timestamp, collector version)

**Dependencies to Install**:
```bash
pip install psutil cpuinfo nvidia-ml-py
```

**Testing**: Create unit tests for each method (see Phase 3)

---

### 1.2 JSON Handler Implementation
**File**: `src/json_handler.py`

- [ ] Implement `save_system_info()` method
  - Accept system_data dict
  - Generate filename with timestamp (YYYY-MM-DD_HH-MM-SS.json)
  - Save to `data/` directory
  - Return full path to saved file

- [ ] Implement `load_system_info()` method
  - Read and parse JSON file
  - Validate JSON structure
  - Return as dict

- [ ] Implement `append_timestamp()` method
  - Add collection_timestamp field
  - Add hostname field
  - Add collector version

- [ ] Implement `validate_json_structure()` method
  - Verify required fields exist
  - Check data types
  - Return validation report

- [ ] Create custom JSON encoder for non-standard types
  - Handle datetime objects
  - Handle bytes objects
  - Handle custom objects

**Testing**: Unit tests for file I/O and serialization

---

### 1.3 Configuration Management Implementation
**File**: `config/config.py`

- [ ] Implement `load_from_file()` method
  - Read settings.json
  - Handle missing file gracefully

- [ ] Implement `load_from_environment()` method
  - Support ITAD_ prefixed environment variables
  - Override file config with env vars

- [ ] Implement `get()` method with nested key support
  - Support "database.type" syntax
  - Return default if key not found

- [ ] Implement `validate()` method
  - Check required fields
  - Validate database type is supported
  - Validate paths are writable

- [ ] Create sample configuration files for different scenarios
  - SQLite (default)
  - SQL Server
  - MySQL
  - PostgreSQL

---

## Phase 2: Database Integration (Priority: HIGH)

### 2.1 Database Manager Implementation
**File**: `src/database.py`

- [ ] Set up SQLAlchemy ORM
  - Create database models/classes
  - Define SystemInfo model with fields:
    - id (Primary Key)
    - hostname (Unique)
    - collection_timestamp (DateTime)
    - cpu_model, cpu_cores, cpu_threads (String, Int, Int)
    - ram_total_gb, ram_available_gb (Float)
    - gpu_model, gpu_memory_gb (String, Float)
    - storage_drives_count, total_storage_gb (Int, Float)
    - os_info (String)
    - full_data (JSON/Text - complete data)
    - created_at, updated_at (DateTime)

- [ ] Implement `connect()` method
  - Support multiple database types
  - Handle connection strings
  - Test connection on initialization

- [ ] Implement `create_tables()` method
  - Use SQLAlchemy declarative base
  - Auto-create schema if not exists
  - Add indexes for efficient querying

- [ ] Implement `insert_system_info()` method
  - Parse system_data dict
  - Create SystemInfo record
  - Handle duplicates (insert or update)
  - Return inserted record ID

- [ ] Implement `update_system_info()` method
  - Find existing record by hostname
  - Update fields
  - Update updated_at timestamp

- [ ] Implement `get_system_info()` and `get_all_systems()` methods
  - Query by hostname or all
  - Return as dict or list

- [ ] Implement `health_check()` method
  - Verify connection is alive
  - Return True/False

**Dependencies to Install**:
```bash
pip install sqlalchemy pyodbc mysql-connector-python psycopg2-binary
```

**Testing**: Database integration tests with test database

---

### 2.2 Error Handling & Logging
**File**: `src/main.py`

- [ ] Implement comprehensive error handling
  - Try-catch for each module
  - Graceful degradation (collect what you can)
  - Detailed error messages

- [ ] Implement `setup_logging()` function
  - Configure console and file logging
  - Use logging module
  - Support log levels from config

- [ ] Create logger for each module
  - system_info.py
  - json_handler.py
  - database.py

---

## Phase 3: Main Program Implementation (Priority: HIGH)

### 3.1 Main Entry Point
**File**: `src/main.py`

- [ ] Implement command-line argument parsing
  - `--config <file>`: Custom config file
  - `--schedule <minutes>`: Enable scheduling
  - `--database-only`: Skip JSON file saving
  - `--json-only`: Skip database upload
  - `--verbose`: Detailed output

- [ ] Implement `main()` function
  - Parse arguments
  - Load config
  - Setup logging
  - Create collectors and handlers
  - Execute workflow
  - Report results
  - Handle errors

- [ ] Create execution workflow
  1. Load configuration
  2. Setup logging
  3. Collect system information
  4. Save to JSON
  5. Upload to database
  6. Report status

- [ ] Add execution status reporting
  - Display what's being collected
  - Progress indicators
  - Summary on completion

---

## Phase 4: Testing & Quality (Priority: MEDIUM)

### 4.1 Unit Tests
**Directory**: `tests/`

- [ ] Create test suite for system_info.py
- [ ] Create test suite for json_handler.py
- [ ] Create test suite for database.py
- [ ] Create test suite for config.py

**Test Coverage Target**: ≥ 80%

### 4.2 Integration Tests
- [ ] Test complete workflow end-to-end
- [ ] Test with different database types
- [ ] Test error scenarios

### 4.3 Code Quality
- [ ] Run flake8 for style violations
- [ ] Run pylint for code analysis
- [ ] Format code with black
- [ ] Add type hints

---

## Phase 5: Documentation & Polish (Priority: MEDIUM)

### 5.1 Documentation
- [ ] Complete docstrings for all functions
- [ ] Create API documentation
- [ ] Create troubleshooting guide
- [ ] Create database schema documentation

### 5.2 Examples
- [ ] Create sample config files
- [ ] Create example output JSON files
- [ ] Create sample database queries

---

## Phase 6: Future Enhancements (Priority: LOW)

### 6.1 Scheduling & Automation
- [ ] Implement periodic collection using APScheduler
- [ ] Create Windows Task Scheduler integration
- [ ] Create cron job templates for Linux

### 6.2 Web Interface
- [ ] Create REST API (FastAPI or Flask)
- [ ] Create web dashboard for viewing data
- [ ] Implement data comparison/visualization

### 6.3 Advanced Features
- [ ] Cloud storage support (AWS S3, Azure Blob)
- [ ] Alert system for anomalies
- [ ] Historical analysis and reporting
- [ ] Data export capabilities

---

## Implementation Priority

### Critical Path (Do These First)
1. **system_info.py** - Core data collection
2. **json_handler.py** - Data persistence
3. **database.py** - Database storage
4. **main.py** - Orchestration
5. **Testing** - Ensure quality

### High Priority (Do Next)
6. Configuration management
7. Error handling and logging
8. Command-line interface
9. Documentation

### Medium Priority (Nice to Have)
10. Scheduling/automation
11. Web interface
12. Advanced analytics

---

## Known Issues & Challenges

### GPU Detection
- **Challenge**: Detecting GPUs is platform-specific and complex
- **Solution**: Start with NVIDIA detection, add others iteratively
- **Fallback**: Log warning if GPU detection fails, continue with other info

### Drive Type Detection (SSD vs HDD)
- **Challenge**: On Windows, requires WMI or registry access
- **Solution**: Use `wmi` module for Windows, `lsblk` for Linux
- **Fallback**: Default to "Unknown" type if detection fails

### Cross-Platform Compatibility
- **Windows**: Use WMI for advanced hardware info
- **Linux**: Use `/proc` filesystem and system commands
- **macOS**: Use system_profiler
- **Solution**: Create platform-specific detector classes

### Database Compatibility
- **Challenge**: Different databases have different SQL dialects
- **Solution**: Use SQLAlchemy for abstraction
- **Testing**: Test with at least SQLite and SQL Server

---

## Testing Checklist

Before moving to next phase, ensure:
- [ ] All unit tests pass
- [ ] Code coverage ≥ 80%
- [ ] All docstrings present
- [ ] No linting errors
- [ ] No type hint violations
- [ ] All functionality documented

---

## Deployment Checklist

Before production use:
- [ ] All tests passing
- [ ] Documentation complete
- [ ] Error handling comprehensive
- [ ] Logging working correctly
- [ ] Database schema validated
- [ ] Security review completed
- [ ] Performance tested
- [ ] Backup/recovery procedures documented

---

## Version Milestones

- **v0.1.0**: Basic system info collection + JSON export
- **v0.2.0**: Database integration
- **v0.3.0**: Full testing + documentation
- **v1.0.0**: Production-ready release
- **v1.1.0**: Scheduling and automation
- **v2.0.0**: Web interface and API

---

## Contact & Support

For questions about development or roadmap changes, contact the ITAD team.
