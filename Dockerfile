# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-dev

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install PDM
RUN pip install pdm

# Install dependencies using PDM
RUN pdm install

# Set the library path
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/:$LD_LIBRARY_PATH

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the FastAPI application
CMD ["pdm", "run", "uvicorn", "src.synapsis.main:app", "--host", "0.0.0.0", "--port", "8000"]
