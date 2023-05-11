# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /sreality_viewer
WORKDIR /usr/src/app

# Copy the requirements file into the container at /sreality_viewer
COPY requirements.txt .
COPY app.py .
COPY templates/index.html ./templates/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

# Expose port 8080 for the Flask app
EXPOSE 8080

# Run the command to start the Flask application
CMD ["python", "app.py"]
