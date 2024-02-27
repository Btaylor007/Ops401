import os
import subprocess

def banner_grab_nc(target_address, target_port):
    try:
        nc_command = f"nc -v {target_address} {target_port}"
        result = subprocess.check_output(nc_command, shell=True, stderr=subprocess.STDOUT, text=True)
        print("Banner Grabbing with Netcat:")
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error with Netcat: {e.output}")

def banner_grab_telnet(target_address, target_port):
    try:
        telnet_command = f"telnet {target_address} {target_port}"
        result = subprocess.check_output(telnet_command, shell=True, stderr=subprocess.STDOUT, text=True)
        print("Banner Grabbing with Telnet:")
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error with Telnet: {e.output}")

def banner_grab_nmap(target_address):
    try:
        nmap_command = f"nmap -p- --open {target_address}"
        result = subprocess.check_output(nmap_command, shell=True, stderr=subprocess.STDOUT, text=True)
        print("Banner Grabbing with Nmap:")
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error with Nmap: {e.output}")

def main():
    target_address = input("Enter the target URL or IP address: ")
    target_port = input("Enter the target port number: ")

    banner_grab_nc(target_address, target_port)
    banner_grab_telnet(target_address, target_port)
    banner_grab_nmap(target_address)

if __name__ == "__main__":
    main()
#attritbutions chatgpt
