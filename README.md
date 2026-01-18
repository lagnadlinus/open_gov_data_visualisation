# GovHack: Factors Influencing Youth Choices

Interactive dashboard visualizing factors that influence education, skills, and training choices of young people.

![Dashboard Preview](docs/dashboard_preview.png)

## Features

- **Interactive Charts**: Powered by Plotly.js for deep diving into Education, Income, Mental Health, and Crime trends.
- **Modern Stack**: Django 4.2 Backend + Parquet Data Layer + Dockerized Deployment.
- **Data Pipeline**: Reproducible ETL process converting ABS datasets to optimized Parquet files.

## Quick Start

### Option 1: Docker (Recommended)

1.  **Build and Run**:
    ```bash
    docker-compose up --build
    ```
2.  **Access**: Open [http://localhost:8000](http://localhost:8000).

### Option 2: Local Python

1.  **Install Dependencies**:
    ```bash
    pip install .
    ```
2.  **Run ETL (Data Processing)**:
    ```bash
    # Process raw CSVs in data/raw -> data/processed
    python -m etl.loaddata
    ```
3.  **Run Server**:
    ```bash
    export DEBUG=True
    export SECRET_KEY=your_dev_secret
    python career_visualizer/manage.py runserver
    ```

## Architecture

- **Backend**: Django (serving JSON API & HTML).
- **Frontend**: Vanilla JS + Plotly.js (fetching data from `/get_data/`).
- **Data**:
    - `data/raw`: Landing zone for CSVs/XLSX.
    - `data/processed`: Parquet files for fast read access.
    - `etl/`: Python package for data transformation.

## Development

- **Tests**: `pytest`
- **Lint**: `flake8` / `black`

## Security

See [SECURITY.md](SECURITY.md) for details on secrets and data handling.
