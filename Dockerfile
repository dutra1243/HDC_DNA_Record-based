# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the src folder to the working directory
COPY src/ .

# Install any dependencies specified in requirements.txt
# RUN pip install -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]