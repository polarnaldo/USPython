#!/usr/bin/python3

# USPython - Author: @polarnaldo (Pol Arnaldo)

import signal
import yaml, argparse
from time import sleep
import os, sys, subprocess

# DEFS

script_directory = os.path.dirname(__file__)

# CTRL+C

def signal_handler(key, frame):
    print(colours.redColour + "\n\n[!] Exiting...\n" + colours.endColour)
    restore_usp_agent()
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

    show_banner()

    print(f"{colours.grayColour}\nOptions:\n{colours.endColour}")

    print(f"{colours.yellowColour}\t[-m]{colours.blueColour} Script mode {colours.yellowColour}(interface | command) {colours.purpleColour}[-m interface | -m command]{colours.purpleColour}{colours.endColour}")
    print(f"{colours.yellowColour}\t[-i]{colours.blueColour} Install the dependencies{colours.endColour}")
    print(f"{colours.yellowColour}\t[-d]{colours.blueColour} Download the USP Agent{colours.endColour}")
    print(f"{colours.yellowColour}\t[-h]{colours.blueColour} Show help\n{colours.endColour}")

def show_banner():
    
    os.system("clear")

    print(f"{colours.yellowColour}\n╦ ╦╔═╗╔═╗┬ ┬┌┬┐┬ ┬┌─┐┌┐┌{colours.endColour}")
    print(f"{colours.yellowColour}║ ║╚═╗╠═╝└┬┘ │ ├─┤│ ││││{colours.endColour}")
    print(f"{colours.yellowColour}╚═╝╚═╝╩   ┴  ┴ ┴ ┴└─┘┘└┘{colours.endColour}")
    print(f"{colours.redColour}\n          Version: 1.0.0\n{colours.endColour}")

    print(f"{colours.purpleColour}[-]{colours.turquoiseColour} Made by Pol Arnaldo (@polarnaldo){colours.endColour}")

def show_menu():

    show_banner()

    print(f"{colours.grayColour}\nOptions:\n{colours.endColour}")
    print(f"{colours.yellowColour}[1]{colours.blueColour} Install Dependencies{colours.endColour}")
    print(f"{colours.yellowColour}[2]{colours.blueColour} Download USP Agent{colours.endColour}")
    print(f"{colours.yellowColour}[3]{colours.blueColour} Create USP Agent{colours.endColour}")
    print(f"{colours.yellowColour}[4]{colours.blueColour} Edit USP Agent{colours.endColour}")
    print(f"{colours.yellowColour}[5]{colours.blueColour} Show USP Agent{colours.endColour}")
    print(f"{colours.yellowColour}[6]{colours.blueColour} Delete USP Agent{colours.endColour}")
    print(f"{colours.yellowColour}[E]{colours.blueColour} Exit{colours.endColour}")

def install_dependencies():

    try:

        os.system("clear")
        
        # Check if Docker is installed
        docker_installed = os.system("docker --version > /dev/null 2>&1")

        # Install or update Docker
        if docker_installed != 0:
            print(f"{colours.greenColour}\n[+]{colours.turquoiseColour} Installing Docker...{colours.endColour}")
            os.system("apt install docker.io -y > /dev/null 2>&1")
            print(f"{colours.greenColour}\n[+] Docker installed successfully!{colours.endColour}")
        else:
            print(f"{colours.greenColour}\n[+]{colours.turquoiseColour} Docker already installed, updating...{colours.endColour}")
            os.system("apt install docker.io -y > /dev/null 2>&1")
            print(f"{colours.greenColour}\n[+] Docker updated successfully!{colours.endColour}")
            ###########################################################################################################################################################sleep(1)

        # Check if Docker Compose is installed
        docker_compose_installed = os.system("docker-compose --version > /dev/null 2>&1")

        # Install or update Docker Compose
        if docker_compose_installed != 0:
            print(f"{colours.greenColour}\n[+]{colours.turquoiseColour} Installing Docker Compose...{colours.endColour}")
            os.system("apt install docker-compose -y > /dev/null 2>&1")
            print(f"{colours.greenColour}\n[+] Docker Compose installed successfully!{colours.endColour}")
        else:
            print(f"{colours.greenColour}\n[+]{colours.turquoiseColour} Docker Compose already installed, updating...{colours.endColour}")
            os.system("apt install docker-compose -y > /dev/null 2>&1")
            print(f"{colours.greenColour}\n[+] Docker Compose updated successfully!{colours.endColour}")
            ###########################################################################################################################################################sleep(1)

        # Check if Git is installed
        git_installed = os.system("git --version >/dev/null 2>&1")

        # Install or update Git
        if git_installed != 0:
            print(f"{colours.greenColour}\n[+]{colours.turquoiseColour} Installing Git...{colours.endColour}")
            os.system("apt install git -y > /dev/null 2>&1")
            print(f"{colours.greenColour}\n[+] Git installed successfully!\n{colours.endColour}")
        else:
            print(f"{colours.greenColour}\n[+]{colours.turquoiseColour} Git already installed.{colours.endColour}")
            ###########################################################################################################################################################sleep(1)

        print(f"{colours.greenColour}\n[+] Dependencies installed successfully!\n{colours.endColour}")
        ###########################################################################################################################################################sleep(3)
                
    except:

        print(f"{colours.redColour}\n[!] Error while installing dependencies.\n{colours.endColour}")
        sleep(3)

def download_usp_agent():

    try:

        show_banner()

        print(f"{colours.grayColour}\nDownload USP Agent:{colours.endColour}")

        # Verifying if the directory exists
        if not os.path.exists(f"{script_directory}/obuspa"):
            # Clone the repository if it doesn't exist
            print(f"{colours.greenColour}\n[+]{colours.turquoiseColour} Downloading USP Agent (Obuspa)...{colours.endColour}")
            os.system(f"git clone https://github.com/BroadbandForum/obuspa.git {script_directory}/obuspa > /dev/null 2>&1")
            print(f"{colours.greenColour}\n[+] Repository cloned successfully.\n{colours.endColour}")
            sleep(3)
        else:
            print(f"{colours.greenColour}\n[+] Repository already exists.\n{colours.endColour}")
            sleep(3)

    except:

        print(f"{colours.redColour}\n[!] Error while downloading USP Agent.\n{colours.endColour}")
        sleep(3)


def verify_usp_agent():

    # Verifying if the directory exists
    if not os.path.exists(f"{script_directory}/obuspa"):
        print(f"{colours.redColour}\n[!] Download the USP Agent\n{colours.endColour}")
        sleep(3)

        return False

    return True

def copy_usp_agent():

    try:

        # Copy files that can be modified (vendor.c, vendor_defs.h and factory-reset.txt)
        os.system(f"cp {script_directory}/obuspa/src/vendor/vendor.c {script_directory}")
        os.system(f"cp {script_directory}/obuspa/src/vendor/vendor_defs.h {script_directory}")
        os.system(f"cp {script_directory}/factory-reset-mqtt.txt {script_directory}/factory-reset-mqtt.txt.bak")
        os.system(f"cp {script_directory}/factory-reset-websockets.txt {script_directory}/factory-reset-websockets.txt.bak")

    except:

        print(f"{colours.redColour}\n[!] Error while copying USP Agent.\n{colours.endColour}")
        sleep(3)

def restore_usp_agent():

    try:

        # Restore vendor.c
        os.system(f"cp {script_directory}/vendor.c {script_directory}/obuspa/src/vendor/vendor.c > /dev/null 2>&1")
        os.system(f"rm -r {script_directory}/vendor.c > /dev/null 2>&1")

        # Restore vendor_defs.h
        os.system(f"cp {script_directory}/vendor_defs.h {script_directory}/obuspa/src/vendor/vendor_defs.h > /dev/null 2>&1")
        os.system(f"rm -r {script_directory}/vendor_defs.h > /dev/null 2>&1")

        # Restore factory-reset-mqtt.txt
        os.system(f"cp {script_directory}/factory-reset-mqtt.txt.bak {script_directory}/factory-reset-mqtt.txt > /dev/null 2>&1")
        os.system(f"rm -r {script_directory}/factory-reset-mqtt.txt.bak > /dev/null 2>&1")

        # Restore factory-reset-websockets.txt
        os.system(f"cp {script_directory}/factory-reset-websockets.txt.bak {script_directory}/factory-reset-websockets.txt > /dev/null 2>&1")
        os.system(f"rm -r {script_directory}/factory-reset-websockets.txt.bak > /dev/null 2>&1")

    except Exception as e:

        print(f"{colours.redColour}\n[!] Error while restoring USP Agent.\n{colours.endColour}")
        sleep(3)

def create_usp_agent():

    try:

        show_banner()

        print(f"{colours.grayColour}\nCreate USP Agent:{colours.endColour}")

        if not verify_usp_agent(): return

        copy_usp_agent()

        # Add basic data to the data model

        while True:
            mtp_options = {"1": "MQTT", "2": "WebSockets"}

            print(f"{colours.yellowColour}\n[+]{colours.purpleColour} Message Transfer Protocol of the USP Agent:\n{colours.endColour}")
            print(f"{colours.yellowColour}[1]{colours.blueColour} MQTT{colours.endColour}")
            print(f"{colours.yellowColour}[2]{colours.blueColour} WebSockets{colours.endColour}")

            mtp_user_option = input(f"{colours.redColour}\n[+]{colours.greenColour} Select an option: {colours.endColour}")
            mtp_selected_option = mtp_options.get(mtp_user_option)

            if mtp_selected_option:
                user_agent_mtp = mtp_selected_option
                break
            else:
                print(f"{colours.redColour}\n[!] Please provide a valid option.{colours.endColour}")

        # BETA

        if user_agent_mtp == "WebSockets":
            print(f"{colours.yellowColour}\n[!] WebSockets is still on beta. Try it again with MQTT.\n{colours.endColour}")
            restore_usp_agent()
            sleep(5)
            return

        print(f"{colours.yellowColour}\n[+]{colours.purpleColour} Basic data for the USP Agent:{colours.endColour}")

        while True:
            endpoint_id_name = input(f"{colours.yellowColour}\n[+]{colours.blueColour} Endpoint ID: {colours.endColour}")
            if endpoint_id_name.strip():
                break
            else:
                print(f"{colours.redColour}\n[!] Please provide a non-empty value for Endpoint ID.{colours.endColour}")

        while True:
            vendor_manufacturer = input(f"{colours.yellowColour}\n[+]{colours.blueColour} Manufacturer: {colours.endColour}")
            if vendor_manufacturer.strip():
                break
            else:
                print(f"{colours.redColour}\n[!] Please provide a non-empty value for Manufacturer.{colours.endColour}")

        while True:
            vendor_product_class = input(f"{colours.yellowColour}\n[+]{colours.blueColour} Product Class: {colours.endColour}")
            if vendor_product_class.strip():
                break
            else:
                print(f"{colours.redColour}\n[!] Please provide a non-empty value for Product Class.{colours.endColour}")

        while True:
            vendor_model_name = input(f"{colours.yellowColour}\n[+]{colours.blueColour} Model Name: {colours.endColour}")
            if vendor_model_name.strip():
                break
            else:
                print(f"{colours.redColour}\n[!] Please provide a non-empty value for Model Name.{colours.endColour}")

        # Add functions to data model

        os.system(r'''sed -i '/int VENDOR_Init(void)/i int GetModelNumber(dm_req_t *req, char *buf, int len);\n' ''' + script_directory + r'''/obuspa/src/vendor/vendor.c''')
        
        find_line="\/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\/\/\*\*"
        
        os.system(r'''awk '/''' + find_line + r'''/ {++count} count==2 && /''' + find_line + r'''/ {print "int GetModelNumber(dm_req_t *req, char *buf, int len)\n{\n\tstrncpy(buf, \"MyModelNumber\", len);\n\treturn USP_ERR_OK;\n}\n"} 1' ''' + script_directory + r'''/obuspa/src/vendor/vendor.c > '''  + script_directory + r'''/obuspa/src/vendor/tmp_vendor.c && mv ''' + script_directory + r'''/obuspa/src/vendor/tmp_vendor.c '''+ script_directory + r'''/obuspa/src/vendor/vendor.c''')

        # Add extra data to the data model

        while True:

            extra_data = input(f"{colours.redColour}\n[?]{colours.greenColour} Do you want to add more data to the data model (y/n)? {colours.endColour}")

            if extra_data == "Y" or extra_data == "y":
    
                while True:

                    print(f"{colours.yellowColour}\n[+]{colours.purpleColour} Extra data for the USP Agent:\n{colours.endColour}")
                    print(f"{colours.yellowColour}[1]{colours.blueColour} Read / Only Data{colours.endColour}")
                    print(f"{colours.yellowColour}[2]{colours.blueColour} Read / Write Data{colours.endColour}")

                    data_type = input(f"{colours.yellowColour}\n[+]{colours.blueColour} Select data type: {colours.endColour}")

                    # Add read only parameter to the data model

                    if data_type == "1":

                        # Input verifications

                        while True:
                            
                            read_only_parameter = input(f"{colours.yellowColour}\n[+]{colours.blueColour} Parameter (e.g - Device.Test.Location): {colours.endColour}")
                            
                            # Verify that there are not whitespaces in the output
                            if ' ' not in read_only_parameter:
                                
                                words = read_only_parameter.split('.')

                                # Verify that there are at least two words and the first word is Device or device
                                if len(words) >= 2 and (words[0].lower() == "Device" or words[0].lower() == "device"):

                                    # Verify that the last word does not finish with any special character 
                                    if read_only_parameter[-1] not in ['.', ',', '-']:

                                        break

                                    else:
                                        print(f"{colours.redColour}\n[!] The parameter must not end: '.', ',', or '-'. Try it again.{colours.endColour}")

                                else:
                                    print(f"{colours.redColour}\n[!] The parameter must have at least two words and the first one must be 'Device'. Try it again.{colours.endColour}")

                            else:
                                print(f"{colours.redColour}\n[!] The parameter must not have whitespaces. Try it again.{colours.endColour}")

                        value = input(f"{colours.yellowColour}\n[+]{colours.blueColour} Value (e.g - Barcelona): {colours.endColour}")

                        # Capitalize the first word
                        capitalized_words = [word.capitalize() for word in words]

                        # Join the words with dots
                        transformed_data = '.'.join(capitalized_words)

                        # Check the result
                        if not (transformed_data.startswith('"') and transformed_data.endswith('"')):
                            transformed_data = '"' + transformed_data + '"'

                        # Clean result
                        transformed_data_clean=transformed_data.replace('"', '')
                        
                        # Var for function
                        test = transformed_data_clean.replace('.', '')

                        # Add functions to data model

                        os.system(r'''sed -i '/int VENDOR_Init(void)/i int Function_''' + test + r'''(dm_req_t *req, char *buf, int len);\n' ''' + script_directory + r'''/obuspa/src/vendor/vendor.c''')
                        
                        find_line="\/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\/\/\*\*"
                        
                        os.system(r'''awk '/''' + find_line + r'''/ {++count} count==2 && /''' + find_line + r'''/ {print "int Function_''' + test + r'''(dm_req_t *req, char *buf, int len)\n{\n\tstrncpy(buf, \"'''+ value + r'''\", len);\n\treturn USP_ERR_OK;\n}\n"} 1' ''' + script_directory + r'''/obuspa/src/vendor/vendor.c > '''  + script_directory + r'''/obuspa/src/vendor/tmp_vendor.c && mv ''' + script_directory + r'''/obuspa/src/vendor/tmp_vendor.c '''+ script_directory + r'''/obuspa/src/vendor/vendor.c''')

                        # Adding read only parameters with functions to vendor.c
                        command_read_only = (
                        r'''sed -i '1,/return USP_ERR_OK;/ {
                        /return USP_ERR_OK;/i\\tint ''' + test + r''' = USP_REGISTER_VendorParam_ReadOnly("'''
                        + transformed_data_clean 
                        + r'''", Function_'''+ test +r''', DM_STRING);'''
                        + r'''\n\tif (''' + test + r''' != USP_ERR_OK){return ''' + test + r''';\}\n
                        }' ''' + script_directory + r"/obuspa/src/vendor/vendor.c"
                        )

                        os.system(command_read_only) 

                        break

                    # Add read write parameter to the data model

                    elif data_type == "2":
                        
                        # Input verifications

                        while True:

                            read_write_parameter = input(f"{colours.yellowColour}\n[+]{colours.blueColour} Parameter (e.g - Device.Test.Location): {colours.endColour}")
                            
                            # Verify that there are not whitespaces in the output
                            if ' ' not in read_write_parameter:
                                
                                words = read_write_parameter.split('.')

                                # Verify that there are at least two words and the first word is Device or device
                                if len(words) >= 2 and (words[0].lower() == "Device" or words[0].lower() == "device"):

                                    # Verify that the last word does not finish with any special character 
                                    if read_write_parameter[-1] not in ['.', ',', '-']:

                                        break

                                    else:
                                        print(f"{colours.redColour}\n[!] The parameter must not end: '.', ',', or '-'. Try it again.{colours.endColour}")

                                else:
                                    print(f"{colours.redColour}\n[!] The parameter must have at least two words and the first one must be 'Device'. Try it again.{colours.endColour}")

                            else:
                                print(f"{colours.redColour}\n[!] The parameter must not have whitespaces. Try it again.{colours.endColour}")

                        value = input(f"{colours.yellowColour}\n[+]{colours.blueColour} Value (e.g - Barcelona): {colours.endColour}")

                        # Capitalize the first word
                        capitalized_words = [word.capitalize() for word in words]

                        # Join the words with dots
                        transformed_data = '.'.join(capitalized_words)

                        # Check the result
                        if not (transformed_data.startswith('"') and transformed_data.endswith('"')):
                            transformed_data = '"' + transformed_data + '"'

                        # Clean result
                        transformed_data_clean=transformed_data.replace('"', '')
                        
                        # Var for function
                        test = transformed_data_clean.replace('.', '')

                        # Adding read write parameters with functions to vendor.c

                        command_readwrite = (
                            r'''sed -i '0,/return USP_ERR_OK;/ {
                            /return USP_ERR_OK;/i\\tint ''' + test + r''' = USP_REGISTER_DBParam_ReadWrite("'''
                            + transformed_data_clean 
                            + r'''", "''' + value +  r'''", NULL, NULL, DM_STRING);'''
                            + r'''\n\tif (''' + test + r''' != USP_ERR_OK){return ''' + test + r''';\}\n
                        }' ''' + script_directory + r"/obuspa/src/vendor/vendor.c"
                        )

                        os.system(command_readwrite)
                        
                        break
                    
                    else:

                        print(f"{colours.redColour}\n[?] - Invalid Option. Try Again...{colours.endColour}")

            elif extra_data == "N" or extra_data == "n":
                
                sleep(3)
                break

            else:

                print(f"{colours.redColour}\n[?] - Invalid Option. Try Again...{colours.endColour}")

        # Edit Vendor Defs
        os.system(f"sed -i 's/#define VENDOR_MODEL_NAME    \"USP Agent\"/#define VENDOR_MODEL_NAME    \"{vendor_model_name}\"/' {script_directory}/obuspa/src/vendor/vendor_defs.h")
        os.system(f"sed -i 's/#define VENDOR_MANUFACTURER  \"Manufacturer\"/#define VENDOR_MANUFACTURER  \"{vendor_manufacturer}\"/' {script_directory}/obuspa/src/vendor/vendor_defs.h")
        os.system(f"sed -i 's/#define VENDOR_PRODUCT_CLASS \"USP Agent\"/#define VENDOR_PRODUCT_CLASS \"{vendor_product_class}\"/' {script_directory}/obuspa/src/vendor/vendor_defs.h")

        # Edit Endpoint ID
        os.system(f"sed -i 's/Device.LocalAgent.EndpointID \"usp-agent-mqtt\"/Device.LocalAgent.EndpointID \"{endpoint_id_name}\"/' {script_directory}/factory-reset-mqtt.txt")
        os.system(f"sed -i 's/Device.LocalAgent.EndpointID \"usp-agent-ws\"/Device.LocalAgent.EndpointID \"{endpoint_id_name}\"/' {script_directory}/factory-reset-websockets.txt")

        # Create Docker Image of USP Agent using Dockerfile located in the script directory
        os.system(f"docker build -t uspagent:{endpoint_id_name} {script_directory}/.")

        # Create Docker Container using the previously build Docker image

        if user_agent_mtp == "MQTT":
            os.system(f"docker run -d -v {script_directory}/factory-reset-mqtt.txt:/obuspa/factory-reset-mqtt.txt --network host --name USPAgent-{endpoint_id_name} uspagent:{endpoint_id_name} obuspa -r /obuspa/factory-reset-mqtt.txt -p -v4 -i lo")

        if user_agent_mtp == "WebSockets":
            os.system(f"docker run -d -v {script_directory}/factory-reset-mqtt.txt:/obuspa/factory-reset-mqtt.txt --network host --name USPAgent-{endpoint_id_name} uspagent:{endpoint_id_name} obuspa -r /obuspa/factory-reset-mqtt.txt -p -v4 -i lo")
            
        restore_usp_agent()

        sleep(3)

    except Exception as e:

        print(f"{colours.redColour}\n[!] Error while creating USP Agent: {str(e)}{colours.endColour}")
        restore_usp_agent()
        sleep(10)


def create_usp_agent_with_yaml(file, repeat):
    try:
        
        repeat = int(repeat)

        if not verify_usp_agent(): return

        # READ THE YAML FILE
        with open(file, 'r') as file:
            data = yaml.safe_load(file)

        # VERIFIY YAML STRUCTURE

        end_point_id = data['usp_agent']['definitions'][0]['end_point_id']
        manufacturer_parameter = data['usp_agent']['definitions'][1]['manufacturer_parameter']
        product_class = data['usp_agent']['definitions'][2]['product_class']
        model_parameter = data['usp_agent']['definitions'][3]['model_parameter']

        default_end_point_id = end_point_id

        # Check for unknown mtp types in the document
        valid_mtp_type = {"websockets", "mqtt"}
        found_mtp_type = {element.get('mtp-type') for element in data.get('usp_agent', {}).get('definitions', []) if 'mtp-type' in element}
        unknown_mtp_type = found_mtp_type - valid_mtp_type

        if unknown_mtp_type:
            for unknown_mtp_type in unknown_mtp_type:
                print(f"Unknown MTP type: '{unknown_mtp_type}' is misspelled in the document.")
            sys.exit(1)

        # BETA

        if "websockets" in found_mtp_type:

            print(f"{colours.yellowColour}\n[!] WebSockets is still on beta. Try it again with MQTT.\n{colours.endColour}")
            restore_usp_agent()
            sys.exit(1)

        # Check for unknown parameter types in the document
        valid_parameter_types = {"Read Only", "Read Write"}
        found_parameter_types = {element['type'] for element in data['usp_agent']['data_model']}
        unknown_parameter_types = found_parameter_types - valid_parameter_types

        if unknown_parameter_types:
            for unknown_parameter_type in unknown_parameter_types:
                print(f"Unknown type: '{unknown_parameter_type}' is misspelled in the document.")
                sys.exit(1)
        
        # Access the data model
        seen_parameters = set()
        duplicate_parameters = set()
        for index, element in enumerate(data['usp_agent']['data_model'], start=1):
            parameter = element['parameter']
            if not parameter.startswith('Device.') or len(parameter.split('.')) < 2:
                print(f"Error: Parameter '{parameter}' on line {index} does not start with 'Device.' or is missing component after '.'.")
                sys.exit(1)
            
            if parameter in seen_parameters:
                duplicate_parameters.add(parameter)
            seen_parameters.add(parameter)

        if duplicate_parameters:
            print("Error: Duplicate parameters found:")
            for parameter in duplicate_parameters:
                print(f"  - {parameter}")
            sys.exit(1)
        
        # CREATE USP AGENT

        for i in range(repeat):

            script_directory = os.path.dirname(__file__)

            copy_usp_agent()

            # Add functions to data model

            os.system(r'''sed -i '/int VENDOR_Init(void)/i int GetModelNumber(dm_req_t *req, char *buf, int len);\n' ''' + script_directory + r'''/obuspa/src/vendor/vendor.c''')
            
            find_line="\/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\/\/\*\*"
            
            os.system(r'''awk '/''' + find_line + r'''/ {++count} count==2 && /''' + find_line + r'''/ {print "int GetModelNumber(dm_req_t *req, char *buf, int len)\n{\n\tstrncpy(buf, \"MyModelNumber\", len);\n\treturn USP_ERR_OK;\n}\n"} 1' ''' + script_directory + r'''/obuspa/src/vendor/vendor.c > '''  + script_directory + r'''/obuspa/src/vendor/tmp_vendor.c && mv ''' + script_directory + r'''/obuspa/src/vendor/tmp_vendor.c '''+ script_directory + r'''/obuspa/src/vendor/vendor.c''')

            for element in data['usp_agent']['data_model']:
                transformed_data_clean = element['parameter']
                test= element['parameter'].replace('.', '')
                value = element['value']

                # Add read only parameter to the data model

                if element['type'] == 'Read Only':
                    
                    # Add functions to data model

                    os.system(r'''sed -i '/int VENDOR_Init(void)/i int Function_''' + test + r'''(dm_req_t *req, char *buf, int len);\n' ''' + script_directory + r'''/obuspa/src/vendor/vendor.c''')
                    
                    find_line="\/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\/\/\*\*"
                    
                    os.system(r'''awk '/''' + find_line + r'''/ {++count} count==2 && /''' + find_line + r'''/ {print "int Function_''' + test + r'''(dm_req_t *req, char *buf, int len)\n{\n\tstrncpy(buf, \"'''+ value + r'''\", len);\n\treturn USP_ERR_OK;\n}\n"} 1' ''' + script_directory + r'''/obuspa/src/vendor/vendor.c > '''  + script_directory + r'''/obuspa/src/vendor/tmp_vendor.c && mv ''' + script_directory + r'''/obuspa/src/vendor/tmp_vendor.c '''+ script_directory + r'''/obuspa/src/vendor/vendor.c''')
                    
                    command_read_only = (
                    r'''sed -i '1,/return USP_ERR_OK;/ {
                    /return USP_ERR_OK;/i\\tint ''' + test + r''' = USP_REGISTER_VendorParam_ReadOnly("'''
                    + transformed_data_clean 
                    + r'''", Function_'''+ test +r''', DM_STRING);'''
                    + r'''\n\tif (''' + test + r''' != USP_ERR_OK){return ''' + test + r''';\}\n
                    }' ''' + script_directory + r"/obuspa/src/vendor/vendor.c"
                    )

                    os.system(command_read_only)        
                    
                # Add read write parameter to the data model

                if element['type'] == 'Read Write':

                    command_readwrite = (
                    r'''sed -i '0,/return USP_ERR_OK;/ {
                    /return USP_ERR_OK;/i\\tint ''' + test + r''' = USP_REGISTER_DBParam_ReadWrite("'''
                    + transformed_data_clean 
                    + r'''", "''' + value + r'''", NULL, NULL, DM_STRING);'''
                    + r'''\n\tif (''' + test + r''' != USP_ERR_OK){return ''' + test + r''';\}\n
                    }' ''' + script_directory + r"/obuspa/src/vendor/vendor.c"
                    )

                    os.system(command_readwrite)

            # Edit Vendor Defs
            os.system(f"sed -i 's/#define VENDOR_MODEL_NAME    \"USP Agent\"/#define VENDOR_MODEL_NAME    \"{model_parameter}\"/' {script_directory}/obuspa/src/vendor/vendor_defs.h")
            os.system(f"sed -i 's/#define VENDOR_MANUFACTURER  \"Manufacturer\"/#define VENDOR_MANUFACTURER  \"{manufacturer_parameter}\"/' {script_directory}/obuspa/src/vendor/vendor_defs.h")
            os.system(f"sed -i 's/#define VENDOR_PRODUCT_CLASS \"USP Agent\"/#define VENDOR_PRODUCT_CLASS \"{product_class}\"/' {script_directory}/obuspa/src/vendor/vendor_defs.h")

            # Edit Endpoint ID
            os.system(f"sed -i 's/Device.LocalAgent.EndpointID \"usp-agent-mqtt\"/Device.LocalAgent.EndpointID \"{end_point_id}\"/' {script_directory}/factory-reset-mqtt.txt")

            # Create Docker Image of USP Agent using Dockerfile located in the script directory
            os.system(f"docker build -t uspagent:{end_point_id} {script_directory}/.")

            # Create Docker Container using the previously built Docker image
            os.system(f"docker run -d -v {script_directory}/factory-reset-mqtt.txt:/obuspa/factory-reset-mqtt.txt --network host --name USPAgent-{end_point_id} uspagent:{end_point_id} obuspa -r /obuspa/factory-reset-mqtt.txt -p -v4 -i lo")

            end_point_id = default_end_point_id + str(i+1)

            restore_usp_agent()

    except Exception as e:

        print(f"{colours.redColour}\n[!] Error while creating USP Agent: {str(e)}\n{colours.endColour}")
        restore_usp_agent()
        sleep(10)

def edit_usp_agent():

    try:

        show_banner()
        print(colours.grayColour + "\nEdit USP Agent:" + colours.endColour)

        os.system("sudo docker exec -it obuspa-mqtt obuspa -c show database")
        sleep(3)

    except Exception as e:

        print(f"{colours.redColour}\n[!] Error while editing USP Agent: {str(e)}{colours.endColour}")
        sleep(3)

def show_usp_agent():

    try:

        show_banner()

        print(f"{colours.grayColour}\nShow USP Agent:{colours.endColour}")

        output = subprocess.check_output("docker ps | grep USPAgent | awk '{print $NF}' | sort", shell=True, text=True)
        lines = output.splitlines()
        num_lines = 0

        print(colours.yellowColour + "\n[+]" + colours.blueColour + " USP Agents list: \n" + colours.endColour)

        for line in lines:
            num_lines = num_lines + 1

            print(f"[{num_lines}] - {line}")

        if num_lines == 0:            
            print(colours.redColour + "[!] There are no USP Agents." + colours.endColour)
            sleep(3)
            return

        print(colours.yellowColour + "\n[+]" + colours.blueColour + " Total USP Agents: " + str(num_lines) + "\n" + colours.endColour)

        sleep(5)

    except Exception as e:

        print(f"{colours.redColour}\n[!] Error while showing USP Agent: {str(e)}{colours.endColour}")
        sleep(3)

def delete_usp_agent():

    try:

        show_banner()

        output = subprocess.check_output("docker ps | grep USPAgent | awk '{print $NF}' | sort", shell=True, text=True)
        lines = output.splitlines()
        num_lines = 0

        print(f"{colours.yellowColour}\n[+]{colours.blueColour} USP Agents list: \n{colours.endColour}")

        for num, line in enumerate(lines, start=1):
            num_lines += 1
            print(f"{num} - {line}")

        if num_lines == 0:            
            print(f"{colours.redColour}[!] There are no USP Agents.{colours.endColour}")
            sleep(3)
            return

        print(f"{colours.yellowColour}\n[+]{colours.blueColour} Total USP Agents: {num_lines}{colours.endColour}")

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

                    os.system(f"docker rm {delete_agent} -f")
                    
                    break

                else:
                    print(f"{colours.redColour}\n[!] Error: The number entered is out of range.{colours.endColour}")

            except ValueError:

                print(f"{colours.redColour}\n[!] Error: Please enter a valid number.{colours.endColour}")

            sleep(3)

    except Exception as e:

        print(f"{colours.redColour}\n[!] Error while deleting USP Agent: {str(e)}{colours.endColour}")
        sleep(3)

def main():

    if not check_root():
        print(f"{colours.redColour}\n[!] You must be root to run this script.\n{colours.endColour}")
        sys.exit(1)

    install_dependencies()

    while True:

        show_menu()

        option = input(f"{colours.redColour}\n[+]{colours.greenColour} Select an option: {colours.endColour}")

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
            print(f"{colours.redColour}\n[!] Exiting...\n{colours.endColour}")
            sleep(1)
            break
        else:
            print(f"{colours.redColour}\n[?] Invalid Option. Try Again...{colours.endColour}")
            sleep(3)

# MAIN

if __name__ == "__main__":
    
    if not check_root():
        print(f"{colours.redColour}\n[!] You must be root to run this script.\n{colours.endColour}")
        sys.exit(1)
        
    parser = argparse.ArgumentParser(description='USPython - Author: @polarnaldo - This program allows you to create a USP agent with YAML.')
    parser.add_argument('-m', '--mode', choices=['interface', 'command'], help="Script mode (interface | command)")
    parser.add_argument('-i', '--install', action='store_true', help='Install  the dependencies')
    parser.add_argument('-d', '--download', action='store_true', help='Download the USP Agent (Obuspa)')
    parser.add_argument('-f', '--file', nargs='?', const='usp-data.yaml', help='Path to YAML file (only applicable in command mode)')
    parser.add_argument('-r', '--repeat', nargs='?', const=1, help='Create multiple agents (only applicable in command mode)')

    args, unknown = parser.parse_known_args()

    file_to_use = args.file if args.file else 'usp-data.yaml'
    repeat_times = args.repeat if args.repeat else 1

    if unknown:
        show_help()
    elif args.mode == "interface":
        main()
    elif args.mode == "command":
        create_usp_agent_with_yaml(file_to_use, repeat_times)
    elif args.install:
        install_dependencies()
    elif args.download:
        download_usp_agent()
    else:
        show_help()