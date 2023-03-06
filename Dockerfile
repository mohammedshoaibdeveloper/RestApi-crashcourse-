# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Set the environment variable for Kafka bootstrap servers
ENV KAFKA_BOOTSTRAP_SERVERS=kafka:9092

# Run the command to start the Django development server
CMD python manage.py runserver 0.0.0.0:8000
