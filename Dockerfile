# Use the official Python image as base
FROM python:alpine

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apk update \
    && apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Command to run the application
CMD ["python3", "main.py"]

ENTRYPOINT ["python3", "main.py"]
