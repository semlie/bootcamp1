# Use an official Python runtime as a parent image
FROM python:3.12.2-alpine3.19

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the .env file into the container at /app
COPY .env /app/.env

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]

#docker run --env-file .env -p 5000:5000 my-python-rest-api
