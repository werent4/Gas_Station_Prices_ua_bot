# Create image with python
FROM python:3 

# Dependencies

# Create workdir in docker
WORKDIR /app

# Copy all files from the current directory (where the Dockerfile is located) inside the container
COPY . .

# Installing dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requierments.txt

# Run
CMD ["python3", "main.py"]
