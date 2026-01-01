# ITAD Enterprise Data Collection

A Python application that collects comprehensive system information (CPU, GPU, RAM, storage, etc.) from machines, converts it to JSON format, and uploads it to a database.

## Project Structure

```
ITAD_ENTERPRISE_Data_collection/
├── src/
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # Main entry point
│   ├── system_info.py           # System hardware collection
│   ├── json_handler.py          # JSON serialization & file I/O
│   └── database.py              # Database operations
├── config/
│   ├── config.py                # Configuration management
│   └── settings.json            # Configuration file
├── data/                        # JSON output files
├── logs/                        # Log files
├── tests/                       # Unit tests
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── DEVELOPMENT.md               # Development roadmap
```

## Features

- **System Information Collection**
  - CPU information (model, cores, threads, frequency)
  - GPU information (NVIDIA, AMD, Intel)
  - RAM information (total, available, used)
  - Storage information (drives, capacity, type)
  - Network information
  - OS and system details

- **Data Processing**
  - Converts collected data to JSON format
  - Timestamped JSON files
  - Custom serialization for complex types

- **Database Integration**
  - Support for multiple database backends (SQLite, MySQL, PostgreSQL, SQL Server)
  - Automatic schema creation
  - Insert, update, and retrieve system information

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ITAD_ENTERPRISE_Data_collection.git
   cd ITAD_ENTERPRISE_Data_collection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the application:
   - Edit `config/settings.json` with your database details
   - Set environment variables if needed

## Usage

### Single Data Collection

```bash
python src/main.py
```

### With Custom Config

```bash
python src/main.py --config /path/to/custom/config.json
```

### View Help

```bash
python src/main.py --help
```

## Configuration

Edit `config/settings.json` to customize:

- **Database**: Choose between SQLite, MySQL, PostgreSQL, or SQL Server
- **Logging**: Set log level and output directory
- **Data Collection**: Enable/disable specific hardware categories
- **Retention**: Configure how long to keep local JSON files

## Database Setup

### SQLite (Default)
No setup required - database will be created automatically.

### SQL Server
```json
{
    "database": {
        "type": "mssql",
        "connection_string": "mssql+pyodbc://user:password@server/database?driver=ODBC+Driver+17+for+SQL+Server"
    }
}
```

### MySQL
```json
{
    "database": {
        "type": "mysql",
        "connection_string": "mysql+pymysql://user:password@localhost:3306/database"
    }
}
```

### PostgreSQL
```json
{
    "database": {
        "type": "postgresql",
        "connection_string": "postgresql://user:password@localhost:5432/database"
    }
}
```

## Development

See `DEVELOPMENT.md` for the complete development roadmap and next steps.

## Architecture

### Data Flow

```
System → SystemInfoCollector → dict → JSONHandler → JSON file
                                     ↓
                                   Database ← DatabaseManager
```

### Module Responsibilities

- **system_info.py**: Hardware detection and information gathering
- **json_handler.py**: JSON serialization and file operations
- **database.py**: Database connectivity and data persistence
- **config.py**: Configuration management
- **main.py**: Orchestration and workflow management

## Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/
```

## Logging

Logs are written to `logs/application.log` by default. Configure logging level in `settings.json`.

## Future Enhancements

- [ ] Scheduled/periodic data collection (APScheduler)
- [ ] REST API for querying collected data
- [ ] Web dashboard for visualization
- [ ] Authentication and security enhancements
- [ ] Cloud storage integration (AWS S3, Azure Blob)
- [ ] Comparison and historical analysis
- [ ] Alert system for anomalies

## Requirements

- Python 3.8+
- See `requirements.txt` for full dependencies

## License

[Your License Here]

## Support

For issues, questions, or contributions, please contact the ITAD team.
