# Use official Python 3.10 slim image as base
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy application file from host to container
COPY app.py .

# Install Flask dependency
RUN pip install flask

# Expose port 5000 for Flask application
EXPOSE 5000

# Run the Flask application when container starts
CMD ["python", "app.py"]