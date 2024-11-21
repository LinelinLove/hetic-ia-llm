FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl https://ollama.com/install.sh | sh

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .
COPY app.py .
COPY entrypoint.sh .

# Install Python dependencies
RUN pip install --no-cache-dir \
    ollama \
    requests

# Make entrypoint executable
RUN chmod +x entrypoint.sh

# Entrypoint handles model pulling
ENTRYPOINT ["/app/entrypoint.sh"]