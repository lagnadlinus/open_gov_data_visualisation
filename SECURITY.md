# Security Policy

We take the security of this open-source project seriously. Given that this repository hosts open government data visualizations, we prioritize data integrity, sanitation, and secure configuration.

## Supported Versions

Only the latest `main` branch is actively supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| Main    | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability within this project, please report it privately.

**Do not open a public GitHub issue.**

Instead, please email the maintainer at `your-email@example.com` (replace with actual email) with a detailed description of the issue. We will strive to acknowledge your report within 48 hours.

## Security Best Practices Audit

This project adheres to the following security standards:

### 1. Secrets Management
*   **No Hardcoded Credentials**: We strictly enforce zero-tolerance for hardcoded secrets. All sensitive keys (`SECRET_KEY`, `DB_PASSWORD`, `API_KEYS`) are loaded via environment variables using `python-dotenv`.
*   **Git Hygiene**: `.env` files and other local configuration files are explicitly excluded in `.gitignore`.

### 2. Data Privacy & Hygiene
*   **Open Data Only**: This project is designed to visualize **publicly available** datasets (e.g., ABS, AIHW).
*   **No PII**: No Personally Identifiable Information (PII) is stored or processed.
*   **Sanitization**: The ETL pipeline (`etl/loaddata.py`) is designed to strip potential metadata outliers, though the primary input source is already anonymized public data.
*   **Git Exclusion**: Raw data directories (`data/`, `datas/`) are git-ignored to prevent accidental uploads of large or unverified files.

### 3. Dependencies
*   **Pinned Versions**: Dependencies are managed via `pyproject.toml` to ensure reproducible and secure builds.
*   **Regular Audits**: We recommend running `pip-audit` or `safety` regularly to check for CVEs in third-party packages.

### 4. Infrastructure
*   **Docker Isolation**: The application runs in a containerized environment, minimizing host system exposure.
*   **Debug Mode**: `DEBUG` is disabled by default in production configurations.

## Disclaimer

This software is provided "as is", without warranty of any kind. Users deploying this dashboard in a public-facing environment should perform their own infrastructure penetration testing.
