FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=career_visualizer.settings

# Set work directory
WORKDIR /app

# Install system dependencies
# gcc and python3-dev might be needed for some python packages
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Copy project
COPY . .

# Run entrypoint
# We'll use a script to handle migrations maybe, or just CMD
EXPOSE 8000

# Default command matches production use
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "career_visualizer", "career_visualizer.wsgi:application"]
