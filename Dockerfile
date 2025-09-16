# Use slim Python image
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc git curl && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements from the api folder
COPY api/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy the ML model (pre-downloaded)
COPY model/ /app/model/

# Copy FastAPI app
COPY api/ /app/api/

# Copy other project files if needed
COPY . /app

# Expose port for Hugging Face Spaces
EXPOSE 7860

# Run FastAPI with uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "7860", "--workers", "1"]
