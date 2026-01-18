<div align="center">

# 📊 GovHack '24: Socioeconomic Insights Dashboard

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br>

**A production-ready data storytelling platform visualising the factors influencing youth education, employment, and mental health choices in Australia.**

[Features](#-key-features) •
[Quick Start](#-quick-start) •
[Tech Stack](#%EF%B8%8F-tech-stack) •
[Architecture](#-architecture)

---
</div>

## 📖 About The Project

This project transforms open government data (ABS, AIHW) into an immersive, interactive experience. It moves beyond static spreadsheets to provide a **living dashboard** where policymakers and the public can explore the correlations between income, education, crime, and mental health.

### 🎯 Key Features

*   **✨ Modern Bento Grid Interface**: A responsive, high-density layout inspired by modern design trends.
*   **🌙 Dark Mode**: Fully supported dark/light themes with accessible high-contrast modes.
*   **📊 Interactive Storytelling**: 
    *   **Consolidated Home View**: See the big picture with cross-correlated charts.
    *   **Deep Dives**: Dedicated tabs for Income, Education, Crime, and Mental Health.
    *   **Zoom & Pan**: Powered by Plotly.js for detailed data exploration.
*   **🗺️ Geospatial & Demographics**: Interactive visualisations of data distribution across Australian states.
*   **📑 Resource Centre**: 
    *   **Smart Print**: Generate clean, full-page PDF reports of the dashboard.
    *   **Downloads**: Access original research papers (PDF) and high-res charts (PNG).
*   **🏗️ Robust Data Pipeline**: Automated ETL process converting raw CSVs to optimised Parquet files.

---

## ⚡ Quick Start

Get the dashboard running in minutes.

### 🐳 Option 1: Docker (Recommended)

The easiest way to run the full stack (App + Data Processing).

```bash
# 1. Clone the repository
git clone https://github.com/lagnadlinus/open_gov_data_visualisation.git
cd open_gov_data_visualisation

# 2. Build and Run
docker-compose up --build
```

> **Access**: Open your browser to [http://localhost:8000](http://localhost:8000)

### 🐍 Option 2: Local Python

For developers wanting to modify the code.

1.  **Install Dependencies**:
    ```bash
    pip install .
    ```

2.  **Run ETL (Data Processing)**:
    ```bash
    # Transforms raw CSV data into optimised Parquet files
    python -m etl.loaddata
    ```

3.  **Run Server**:
    ```bash
    export DEBUG=True
    export SECRET_KEY=dev_secret_key
    python career_visualizer/manage.py runserver
    ```

---

## 🛠️ Tech Stack

Built with a focus on performance, scalability, and maintainability.

| Layer | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | ![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white) | Robust web framework serving JSON APIs and HTML. |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) ![JS](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black) | Semantic HTML + Vanilla JS for lightweight interactivity. |
| **Viz** | ![Plotly](https://img.shields.io/badge/Plotly.js-3F4F75?logo=plotly&logoColor=white) | High-performance interactive charting library. |
| **Data** | ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) ![Parquet](https://img.shields.io/badge/Apache%20Parquet-478546?logo=apache&logoColor=white) | ETL processing and optimized columnar storage. |
| **Ops** | ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) | Containerized deployment environment. |

---

## 🏗 Architecture

```mermaid
graph LR
    A["Raw Data (CSV)"] -->|ETL Script| B("Processed Parquet")
    B -->|Pandas| C[Django Views]
    C -->|JSON API| D["Frontend (Plotly.js)"]
    
    subgraph Data Layer
    A
    B
    end
    
    subgraph Application
    C
    D
    end
```

## 🔒 Security

We take data security seriously.
*   **Secrets Management**: No hardcoded secrets; environment variables used for configuration.
*   **Data Hygiene**: automated cleanup of raw sensitive files.
*   See [SECURITY.md](SECURITY.md) for our full policy.

---

<div align="center">
    Made with ❤️ for GovHack '24
</div>
