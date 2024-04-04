# Use an official Python runtime as the base image
FROM python:3.11.4

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining application code to the container
COPY . .

# Copy the custom entrypoint script
COPY custom/entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["entrypoint.sh"]

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set the command to run your Flask app
CMD ["python", "app.py"]