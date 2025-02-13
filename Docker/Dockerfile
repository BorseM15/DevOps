# Use official Python runtime as a base image
FROM python:3.9
 
# Set the working directory
WORKDIR /app
 
# Copy all files to the container
COPY . /app
 
# Install Flask
RUN pip install flask
 
# Expose port 5000
EXPOSE 5000
 
# Run the Flask application
CMD ["python", "app.py"]