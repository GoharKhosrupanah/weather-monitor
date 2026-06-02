FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8000

# Default command for API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]