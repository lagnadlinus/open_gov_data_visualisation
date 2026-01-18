# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

Please report security vulnerabilities by emailing the maintainer directly. Do not open public issues for sensitive security problems.

## Secrets Management

- **NEVER** commit secrets (API keys, credentials, database passwords) to git.
- Use `.env` files for local development. Copy `.env.example` (if provided) to `.env` and fill in your values.
- In production, inject secrets via environment variables.
- `SECRET_KEY` and `DEBUG` settings in Django are configured to read from environment variables.

## Data Policy

- This project uses **Open Public Data** (ABS, etc.).
- **DO NOT** add private, PII, or sensitive data to this repository.
- Raw data files in `data/raw` and processed data in `data/processed` are git-ignored to prevent accidental leaks of large internal datasets if they were ever added (though open data is fine to track if small, we ignore for size).

## Dependency Management

- Dependencies are pinned in `pyproject.toml`.
- Use `pip install .` or Docker to ensure consistent environments.
- Regularly audit dependencies for vulnerabilities (e.g., using `safety` or GitHub Dependabot).
