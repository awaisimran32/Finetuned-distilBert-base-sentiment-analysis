FROM python:3.10-slim

# system deps (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc git curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copy api requirements and install
COPY api/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# copy project
COPY . /app

# port
EXPOSE 8000

# Use env var to set host/port in uvicorn if you want later
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
