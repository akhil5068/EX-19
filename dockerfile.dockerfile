# Use Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt requirements.txt
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "app.py"]
