# Build stage
FROM python:alpine as builder

WORKDIR /app

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:alpine

WORKDIR /app

# Copy only the necessary files from builder
COPY --from=builder /usr/local/lib/python3.*/site-packages/ /usr/local/lib/python3.*/site-packages/
COPY . .

# Remove unnecessary files
RUN rm -rf __pycache__ *.pyc *.pyo *.pyd .Python

ENTRYPOINT ["python3", "main.py"]
