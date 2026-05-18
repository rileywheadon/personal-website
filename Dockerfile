# Keep this pinned to the same version as my virtual environment
FROM python:3.14-slim
WORKDIR /app

# Install dependencies first for better build caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a nonroot user for improved security
RUN useradd -m appuser

# Only copy what is strictly necessary to reduce image size
COPY ./blog ./blog
COPY ./app.py ./app.py

# Transfer ownership to the nonroot user
RUN chown -R appuser:appuser /app
USER appuser

# Expose application port and run app
EXPOSE 8000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000", "--workers", "4"]
