# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /sreality_viewer
WORKDIR /

# Copy the requirements file into the container at /sreality_viewer
COPY requirements.txt /

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV DATABASE_URL=postgresql://postgres:Praha123@localhost:5432/sreality

# Expose port 8080 for the Flask app
EXPOSE 8080

# Run the command to start the Flask application
CMD ["python", "app.py"]
