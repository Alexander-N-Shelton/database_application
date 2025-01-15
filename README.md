# Database Application

## Overview
`database_application` is a Python-based GUI application designed to connect to a PostgreSQL database and 
present an interactive interface for managing and viewing various datasets. 
This application uses the `tkinter` library for the GUI and loads initial data from CSV files.

## Features
- Connects to a PostgreSQL database for viewing data.
- Uses initial data from CSV files (`IN450A.csv`, `IN450B.csv`, `IN450C.csv`) to populate database tables.
- Provides a user-friendly GUI for data interaction.

## Requirements
- Python 3.x
- PostgreSQL
- `psycopg2` (for connecting to PostgreSQL)

## Installation

### Step 1: Clone the Repository
First, clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/database_application.git
cd database_application
```

### Step 2: Set Up a Virtual Environment (recommended)
To isolate dependencies, set up a virtual environment:
```bash
python3 -m venv env
source env/bin/activate  # Use `env\Scripts\activate` on Windows
```

### Step 3: Build and Install the Package
In the root directory of the project, build and install the package:
```bash
python setup.py sdist bdist_wheel
pip install dist/database_application-0.1-py3-none-any.whl
```

### Step 4: Configure the Database
1. **Run the SQL Script**: Use `schema.sql` to set up tables in your PostgreSQL database.
   - For example, in `psql`:
     ```sql
     \i sql/schema.sql
     ```
   
2. **Load Initial Data** (optional): Load data from the provided CSV files (`data/IN450A.csv`, `data/IN450B.csv`, `data/IN450C.csv`) into your database tables if needed. This can be done using `COPY` commands in SQL or through a database client like pgAdmin.
The .csv files are located in the data/ directory.

## Running the Application
After installation, you can start the application by running:
```bash
start_app
```

This command will open the GUI, allowing you to view and interact with the data in your PostgreSQL database.

## Troubleshooting
- **Database Connection Issues**: Ensure your PostgreSQL database credentials are correctly set as environment variables (e.g., `DB_USER`, `DB_PASSWORD`, etc.) before starting the application.
- **Data Loading**: If CSV data doesn’t load automatically, try loading it manually using SQL `COPY` commands.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
If you’d like to contribute, please fork the repository and use a feature branch. Pull requests are welcome!

## Changelog
All notable changes to this project will be documented in this file.
