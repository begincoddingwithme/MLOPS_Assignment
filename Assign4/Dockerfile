# Stage 1: Build Stage
FROM python:3.11-slim AS builder

# Set the working directory
WORKDIR /my_app

# Copy only the requirements file to optimize caching
COPY requirements.txt .

# Install dependencies
RUN pip install --user -r requirements.txt

# Stage 2: Runtime Stage
FROM python:3.11-slim

# Set the working directory
WORKDIR /my_app

# Copy necessary files from the builder stage
COPY --from=builder /root/.local /root/.local
COPY . .

# Update PATH to include pip-installed binaries
ENV PATH=/root/.local/bin:$PATH

# Expose the application port
EXPOSE 8000

# Set the entry point to your application
CMD ["python", "app.py"]
