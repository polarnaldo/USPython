#!/bin/bash

# USPython - Author: @polarnaldo (Pol Arnaldo)

# CTRL+C

function ctrl_c (){
  echo -e "${redColour}\n\n[!] Exiting...\n${endColour}"
  tput cnorm && exit 1
}

trap ctrl_c INT

# COLOURS

#greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
#blueColour="\e[0;34m\033[1m"
#yellowColour="\e[0;33m\033[1m"
#purpleColour="\e[0;35m\033[1m"
#turquoiseColour="\e[0;36m\033[1m"
#grayColour="\e[0;37m\033[1m"

# CHECK ROOT

if [ "$(id -u)" -ne 0 ]; then
    echo -e "${redColour}\n[!] You must be root to run this script.\n${endColour}"
    tput cnorm && exit 1
fi

# Pull the latest Ubuntu image
docker pull ubuntu:latest

# Run a container from the Ubuntu image in detached mode with a custom name 'USPython' and share the Docker socket and binary
docker run -dit --name USPython -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/usr/bin/docker ubuntu:latest

# Update package lists and install necessary packages in the running container
docker exec USPython bash -c "apt-get update && apt-get install -y sudo git docker-compose python3 python3-yaml"

# Clone the specified GitHub repository into the container
docker exec USPython bash -c "git clone https://github.com/polarnaldo/USPython"

# Run the specified Python script within the container
docker exec -it USPython bash -c "python3 /USPython/USPython.py -m interface"