FROM python:3.10-slim

# system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl https://ollama.com/install.sh | sh

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY entrypoint.sh .

RUN pip install --no-cache-dir \
    ollama \
    requests

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]