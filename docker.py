#  Docker Basic

'''
    Docker:
        Docker is a powerful platform for developing, shipping, and running applications inside 
        lightweight, portable containers.

    Container:
        Containers are lightweight, isolated environments that include everything an application needs to run, 
        including libraries, system tools, and runtime.

    Image: 
        A lightweight, standalone, and executable package that includes the application code and its dependencies.

    Container: 
        A running instance of a Docker image.

    Dockerfile: 
        A script to define how an image is built.
    
    Docker Hub: 
        A cloud-based registry to store and share Docker images.

    Docker Compose:
        Docker Compose allows you to manage multi-container applications.


    Basic Docker Commands:
        a. Check Docker Info (Gives detailed information about Docker installation.)
            -- docker info
            
        b. Pull an Image (Downloads the hello-world image from Docker Hub.)
            -- docker pull hello-world
        
        c. Run a Container (Starts a container from the hello-world image.)
            -- docker run hello-world
        
        d. List Running Containers (Displays running containers.)
            -- docker ps
        
        e. List All Containers
            -- docker ps -a

        f. Stop a Container
            -- docker stop <container_id>

        g. Remove a Container
            -- docker rm <container_id>

        h. Remove an Image
            -- docker rmi <image_id>

        i. Remove unused containers:
            docker container prune
        
        j. Remove unused images:
            docker image prune

    Creating Your First Docker Image
        Create a Project Folder:
            mkdir my-docker-app
            cd my-docker-app
        
        Create a Simple Application: Create a file named app.py:
            print("Hello, Docker!")
        
        Create a Dockerfile: Create a file named Dockerfile (no extension) with the following content:
            # Use an official Python runtime as the base image
            FROM python:3.9-slim

            # Set the working directory
            WORKDIR /app

            # Copy the current directory contents into the container
            COPY . /app

            # Run the application
            CMD ["python", "app.py"]
        
        Build the Image:
            docker build -t my-python-app .
        
        Run the Container:
            docker run my-python-app
'''

#  Docker Advanced
'''
    Docker Networking:
        a. Bridge Network
            Docker containers are isolated but can communicate through the bridge network.

    Docker Volumes:
        Volumes are used to persist data outside containers.

    Docker Swarm:
        Swarm enables you to manage a cluster of Docker nodes.
'''
import math

# Parameters for the sinusoidal wave
amplitude = 1  # Amplitude of the sine wave
frequency = 1  # Frequency of the sine wave
sample_rate = 100  # Number of samples per cycle
duration = 2  # Duration of the wave in seconds

# Calculate the number of samples based on sample rate and duration
num_samples = sample_rate * duration

# Generate the x values (time) and corresponding y values (sinusoidal)
x_values = []
y_values = []

for i in range(num_samples):
    t = i / sample_rate  # Time variable
    x_values.append(t)
    y_values.append(amplitude * math.sin(2 * math.pi * frequency * t))

# Printing the x (time) and y (sin values) values
for t, y in zip(x_values, y_values):
    print(f"{t:.2f}: {y:.2f}")
