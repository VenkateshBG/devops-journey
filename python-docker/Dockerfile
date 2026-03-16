# Step 1 - Start from official Python image
FROM python:3.11-slim

# Step 2 - Set working directory inside container
WORKDIR /app

# Step 3 - Copy requirements first
COPY requirements.txt .

# Step 4 - Install dependencies
RUN pip install -r requirements.txt

# Step 5 - Copy our Python script into container
COPY app.py .

# Step 6 - Run the script when container starts
CMD ["python3", "app.py"]
