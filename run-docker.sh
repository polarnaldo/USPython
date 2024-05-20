#!/bin/bash

# Pull the latest Ubuntu image
docker pull ubuntu:latest

# Run a container from the Ubuntu image in detached mode with a custom name 'USPython' and share the Docker socket and binary
docker run -dit --name USPython -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker ubuntu:latest

# Update package lists and install necessary packages in the running container
docker exec USPython bash -c "apt-get update && apt-get install -y sudo git docker-compose python3 python3-yaml"

# Clone the specified GitHub repository into the container
docker exec USPython git clone https://github.com/polarnaldo/USPython

# Run the specified Python script within the container
docker exec -it USPython python3 /USPython/USPython.py -m interface
