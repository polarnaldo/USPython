#!/usr/bin/python3

# USPython - Author: @polarnaldo (Pol Arnaldo)

import signal
from time import sleep
import os, sys, subprocess

# CTRL+C

def signal_handler(key, frame):
    print(colours.redColour + "\n\n[!] - Exiting...\n" + colours.endColour)
    sys.exit(1)

signal = signal.signal(signal.SIGINT, signal_handler)

# COLOURS

class colours:
    greenColour = "\033[0;32m\033[1m"
    endColour = "\033[0m"
    redColour = "\033[0;31m\033[1m"
    blueColour = "\033[0;34m\033[1m"
    yellowColour = "\033[0;33m\033[1m"
    purpleColour = "\033[0;35m\033[1m"
    turquoiseColour = "\033[0;36m\033[1m"
    grayColour = "\033[0;37m\033[1m"

# FUNCTIONS

def check_root():
    return os.geteuid() == 0

def show_help():

    os.system("clear")
    print("=== Docker Installation Script ===")
    print("1. Install Docker")
    print("2. Exit")

def show_banner():
    
    os.system("clear")

    print(colours.yellowColour + "\n╦ ╦╔═╗╔═╗┬ ┬┌┬┐┬ ┬┌─┐┌┐┌" + colours.endColour)
    print(colours.yellowColour + "║ ║╚═╗╠═╝└┬┘ │ ├─┤│ ││││" + colours.endColour)
    print(colours.yellowColour + "╚═╝╚═╝╩   ┴  ┴ ┴ ┴└─┘┘└┘" + colours.endColour)
    print(colours.redColour + "\n          Version: 1.0.0\n" + colours.endColour)

    print(colours.greenColour + "[@]" + colours.turquoiseColour +" - Made by Pol Arnaldo (@polarnaldo)" + colours.endColour)

def show_menu():

    show_banner()

    print(colours.grayColour + "\nOptions:\n" + colours.endColour)
    print(colours.yellowColour + "[1]" + colours.blueColour + " - Install Dependencies" + colours.endColour)
    print(colours.yellowColour + "[2]" + colours.blueColour + " - Download USP Agent" + colours.endColour)
    print(colours.yellowColour + "[3]" + colours.blueColour + " - Create USP Agent" + colours.endColour)
    print(colours.yellowColour + "[4]" + colours.blueColour + " - Edit USP Agent" + colours.endColour)
    print(colours.yellowColour + "[5]" + colours.blueColour + " - Show USP Agent" + colours.endColour)
    print(colours.yellowColour + "[6]" + colours.blueColour + " - Delete USP Agent"  + colours.endColour)
    print(colours.yellowColour + "[E]" + colours.blueColour + " - Exit"  + colours.endColour)

def install_dependencies():
    try:
        os.system("clear")
        
        # Check if Docker is installed
        docker_installed = os.system("docker --version > /dev/null 2>&1")

        # Install or update Docker
        if docker_installed != 0:
            print(colours.greenColour + "\n[+]" + colours.turquoiseColour + " - Installing Docker..." + colours.endColour)
            os.system("apt install docker.io -y > /dev/null 2>&1")
            print(colours.greenColour + "\n[+] - Docker installed successfully!" + colours.endColour)
        else:
            print(colours.greenColour + "\n[+]" + colours.turquoiseColour + " - Docker already installed, updating..." + colours.endColour)
            os.system("apt install docker.io -y > /dev/null 2>&1")
            print(colours.greenColour + "\n[+] - Docker updated successfully!" + colours.endColour)
            ###########################################################################################################################################################sleep(1)

        # Check if Docker Compose is installed
        docker_compose_installed = os.system("docker-compose --version > /dev/null 2>&1")

        # Install or update Docker Compose
        if docker_compose_installed != 0:
            print(colours.greenColour + "\n[+]" + colours.turquoiseColour + " - Installing Docker Compose..." + colours.endColour)
            os.system("apt install docker-compose -y > /dev/null 2>&1")
            print(colours.greenColour + "\n[+] - Docker Compose installed successfully!" + colours.endColour)
        else:
            print(colours.greenColour + "\n[+]" + colours.turquoiseColour + " - Docker Compose already installed, updating..." + colours.endColour)
            os.system("apt install docker-compose -y > /dev/null 2>&1")
            print(colours.greenColour + "\n[+] - Docker Compose updated successfully!" + colours.endColour)
            ###########################################################################################################################################################sleep(1)

        # Check if Git is installed
        git_installed = os.system("git --version >/dev/null 2>&1")

        # Install or update Git
        if git_installed != 0:
            print(colours.greenColour + "\n[+]" + colours.turquoiseColour + " - Installing Git..." + colours.endColour)
            os.system("apt install git -y > /dev/null 2>&1")
            print(colours.greenColour + "\n[+] - Git installed successfully!" + colours.endColour)
        else:
            print(colours.greenColour + "\n[+]" + colours.turquoiseColour + " - Git already installed." + colours.endColour)
            ###########################################################################################################################################################sleep(1)
        
        print(colours.greenColour + "\n[+] - Dependencies installed successfully!" + colours.endColour)
        ###########################################################################################################################################################sleep(3)
    except:
        print(colours.redColour + "[!] - Error while installing dependencies." + colours.endColour)
        sleep(3)

def download_usp_agent():
    try:
        show_banner()

        # Verifying if the directory exists
        if not os.path.exists("obuspa"):
            # Clone the repository if it doesn't exist
            print(colours.greenColour + "\n[+]" + colours.turquoiseColour + " - Downloading USP Agent (Obuspa)..." + colours.endColour)
            os.system("git clone https://github.com/BroadbandForum/obuspa.git > /dev/null 2>&1")
            print(colours.greenColour + "\n[+] - Repository cloned successfully." + colours.endColour)
            sleep(3)
        else:
            print(colours.greenColour + "\n[+] - Repository already exists." + colours.endColour)
            sleep(3)
    except:
        print(colours.redColour + "[!] - Error while downloading USP Agent." + colours.endColour)
        sleep(3)

def create_usp_agent():
    try:
        show_banner()

        script_directory = os.path.dirname(__file__)

        # Copy Default
        os.system("cp {}/obuspa/src/vendor/vendor.c {}".format(script_directory, script_directory))
        os.system("cp {}/obuspa/src/vendor/vendor_defs.h {}".format(script_directory, script_directory))
        os.system("cp {}/factory-reset-mqtt.txt {}/factory-reset-mqtt.txt.bak".format(script_directory,script_directory))
        

        while True:
            endpoint_id_name = input(str(colours.yellowColour + "\n[+]" + colours.blueColour + " - Define the endpoint_id_name: "  + colours.endColour ))
            if endpoint_id_name.strip():
                break
            else:
                print(colours.redColour + "\n[!] - Please provide a non-empty value for endpoint_id_name." + colours.endColour)

        while True:
            vendor_manufacturer = input(str(colours.yellowColour + "\n[+]" + colours.blueColour + " - Define the VENDOR_MANUFACTURER: "  + colours.endColour ))
            if vendor_manufacturer.strip():
                break
            else:
                print(colours.redColour + "\n[!] - Please provide a non-empty value for VENDOR_MANUFACTURER." + colours.endColour)

        while True:
            vendor_product_class = input(str(colours.yellowColour + "\n[+]" + colours.blueColour + " - Define the VENDOR_PRODUCT_CLASS: "  + colours.endColour ))
            if vendor_product_class.strip():
                break
            else:
                print(colours.redColour + "\n[!] - Please provide a non-empty value for VENDOR_PRODUCT_CLASS." + colours.endColour)

        while True:
            vendor_model_name = input(str(colours.yellowColour + "\n[+]" + colours.blueColour + " - Define the VENDOR_MODEL_NAME: "  + colours.endColour ))
            if vendor_model_name.strip():
                break
            else:
                print(colours.redColour + "\n[!] - Please provide a non-empty value for VENDOR_MODEL_NAME." + colours.endColour)

        while True:
            exta_data = input(str("Do you want to add more data to the data model? (y/n)"))

            if exta_data == "Y" or exta_data == "y":
                
                while True:

                    data_type = input(str("Which data type do you want to add to the data model (1-READ/ONLY DATA | 2-READ/WRITE DATA)?"))

                    if data_type == "1":

                        while True:
                            read_only_data = input("Escribe los datos adicionales (por ejemplo, \"Device.Prueba.Prueba\"): ")
                            # Verificar si hay espacios en los datos ingresados
                            if ' ' not in read_only_data:
                                # Dividir la cadena en palabras separadas por '.'
                                words = read_only_data.split('.')
                                # Verificar si hay al menos dos palabras y la primera palabra es "device" o "Device"
                                if len(words) >= 2 and words[0].lower() == "device":
                                    # Verificar si la cadena termina con caracteres especiales
                                    if read_only_data[-1] not in ['.', ',', '-']:
                                        break
                                    else:
                                        print("La cadena no debe terminar con '.', ',', o '-'. Inténtalo de nuevo.")
                                else:
                                    print("Deben haber al menos dos palabras y la primera palabra debe ser 'device'. Inténtalo de nuevo.")
                            else:
                                print("No se permiten espacios en los datos. Inténtalo de nuevo.")

                        # Capitalizar la primera letra de cada palabra
                        capitalized_words = [word.capitalize() for word in words]

                        # Unir las palabras con puntos
                        transformed_data = '.'.join(capitalized_words)

                        # Comprobar si el resultado transformado está entre comillas dobles y agregarlas si no lo está
                        if not (transformed_data.startswith('"') and transformed_data.endswith('"')):
                            transformed_data = '"' + transformed_data + '"'

                        transformed_data_clean=transformed_data.replace('"', '')


                        print("Output:", transformed_data)
                        print(transformed_data_clean)
                        
                        sleep(3)

                        # INSERTAR VARIABLES
                        # sed -i '/int VENDOR_Init(void)/i int GetModelNumber(dm_req_t *req, char *buf, int len);\n' vendor.c
                        # INSERTAR FUNCION
                        # sed -i '/int VENDOR_Init(void)/{N;/{/{N;s/$/\tint CardUnlock = USP_REGISTER_DBParam_ReadWrite("Device.SmartLock.Features.CardUnlock", "MyModelNumber", NULL, NULL, DM_STRING);\n\tif (CardUnlock != USP_ERR_OK)\n\t{\n\t\treturn CardUnlock;\n\t}\n/}}' vendor.c
                        
                        break
                    elif data_type == "2":
                        print("READ/WRITE")
                        sleep(3)
                        break
                    else:
                        print(colours.redColour + "\n[?] - Invalid Option. Try Again..." + colours.endColour)        

            elif exta_data == "N" or exta_data == "n":
                print("No")
                sleep(3)
                break
            else:
                print(colours.redColour + "\n[?] - Invalid Option. Try Again..." + colours.endColour)

        # Edit Vendor Defs
        os.system("sed -i 's/#define VENDOR_MODEL_NAME    \"USP Agent\"/#define VENDOR_MODEL_NAME    \"{}\"/' {}/obuspa/src/vendor/vendor_defs.h".format(vendor_model_name, script_directory))
        os.system("sed -i 's/#define VENDOR_MANUFACTURER  \"Manufacturer\"/#define VENDOR_MANUFACTURER  \"{}\"/' {}/obuspa/src/vendor/vendor_defs.h".format(vendor_manufacturer, script_directory))
        os.system("sed -i 's/#define VENDOR_PRODUCT_CLASS \"USP Agent\"/#define VENDOR_PRODUCT_CLASS \"{}\"/' {}/obuspa/src/vendor/vendor_defs.h".format(vendor_product_class, script_directory))
        
        # Edit Endpoint ID
        os.system("sed -i 's/Device.LocalAgent.EndpointID \"usp-agent-mqtt\"/Device.LocalAgent.EndpointID \"{}\"/' {}/factory-reset-mqtt.txt".format(endpoint_id_name, script_directory))

        # Create Docker Image of USP Agent using Dockerfile located in the script directory
        os.system("docker build -t uspagent:{} {}/.".format(endpoint_id_name, script_directory))

        # Create Docker Container using the previously build Docker image
        os.system("docker run -d -v {}/factory-reset-mqtt.txt:/obuspa/factory-reset-mqtt.txt --network host --name USPAgent-{} uspagent:{} obuspa -r /obuspa/factory-reset-mqtt.txt -p -v4 -i lo".format(script_directory, endpoint_id_name, endpoint_id_name))
        
        # Restore Default
        os.system("cp {}/vendor_defs.h {}/obuspa/src/vendor/vendor_defs.h".format(script_directory, script_directory))
        os.system("rm -r {}/vendor_defs.h".format(script_directory))
        
        os.system("cp {}/vendor.c {}/obuspa/src/vendor/vendor.c".format_map(script_directory, script_directory))
        os.system("rm -r {}/vendor.c". format(script_directory))

        os.system("cp {}/factory-reset-mqtt.txt.bak {}/factory-reset-mqtt.txt".format(script_directory, script_directory))
        os.system("rm -r {}/factory-reset-mqtt.txt.bak".format(script_directory))

        sleep(3)

    except:
        print(colours.redColour + "[!] - Error while creating USP Agent." + colours.endColour)
        sleep(3)

def edit_usp_agent():
    try:
        show_banner()
        os.system("sudo docker exec -it obuspa-mqtt obuspa -c show database")
        sleep(3)
    except:
        print(colours.redColour + "[!] - Error while editing USP Agent." + colours.endColour)
        sleep(3)

def show_usp_agent():
    try:
        show_banner()

        output = subprocess.check_output("docker ps | grep USPAgent | awk '{print $NF}' | sort", shell=True, text=True)
        lines = output.splitlines()
        num_lines = 0

        print(colours.yellowColour + "\n[+]" + colours.blueColour + " - USP Agents list: \n" + colours.endColour)

        for line in lines:
            num_lines = num_lines + 1

            print(f"[{num_lines}] - {line}")

        if num_lines == 0:            
            print(colours.redColour + "[!] - There are no USP Agents." + colours.endColour)
            sleep(3)
            return

        print(colours.yellowColour + "\n[+]" + colours.blueColour + " - Total USP Agents: " + str(num_lines) + "\n" + colours.endColour)

        sleep(5)

    except:
        print(colours.redColour + "[!] - Error while showing USP Agent." + colours.endColour)
        sleep(3)

def delete_usp_agent():
    try:
        show_banner()

        output = subprocess.check_output("docker ps | grep USPAgent | awk '{print $NF}' | sort", shell=True, text=True)
        lines = output.splitlines()
        num_lines = 0

        print(colours.yellowColour + "\n[+]" + colours.blueColour + " - USP Agents list: \n" + colours.endColour)

        for line in lines:
            num_lines = num_lines + 1

            print(str(num_lines) + " - " + str(line))

        if num_lines == 0:            
            print(colours.redColour + "[!] - There are no USP Agents." + colours.endColour)
            sleep(3)
            return

        print(colours.yellowColour + "\n[+]" + colours.blueColour + " - Total USP Agents: " + str(num_lines) + colours.endColour)

        while True:
            try:
                delete = int(input("\nWhich USP Agent do you want to delete? "))
                if 1 <= delete <= num_lines:

                    if num_lines == 0:            
                        print("\nThere are no USP Agents.")
                        sleep(3)
                        return
                    
                    delete_agent = lines[delete - 1]
                    
                    print(f"\nSelected USP Agent to delete: {delete_agent}")

                    os.system("docker rm {} -f".format(delete_agent))
                    
                    break

                else:
                    print(colours.redColour + "\n[!] - Error: The number entered is out of range." + colours.endColour)
            except ValueError:
                print(colours.redColour + "\n[!] -Error: Please enter a valid number." + colours.endColour)

            sleep(3)

    except:
        print(colours.redColour + "[!] - Error while deleting USP Agent." + colours.endColour)
        sleep(3)

# MAIN

if __name__ == "__main__":

    if not check_root():
        print(colours.redColour + "\n[!] - You must be root to run this script.\n" + colours.endColour)
        sys.exit(1)

    install_dependencies()

    while True:

        show_menu()

        option = input(str(colours.redColour + "\n[+]" + colours.greenColour + " - Select an option: " + colours.endColour))

        if option == "1":
            install_dependencies()
        elif option == "2":
            download_usp_agent()
        elif option == "3":
            create_usp_agent()
        elif option == "4":
            edit_usp_agent()
        elif option == "5":
            show_usp_agent()
        elif option == "6":
            delete_usp_agent()
        elif option == "H":
            show_help() 
        elif option == "E":
            os.system("clear")
            show_banner()
            print(colours.redColour + "\n[!] - Exiting...\n" + colours.endColour)
            sleep(1)
            break
        else:
            print(colours.redColour + "\n[?] - Invalid Option. Try Again..." + colours.endColour)
            sleep(3)