
import os import subprocess 
def port_scan(target_ip): """Scans for open ports on the target IP address.""" for port in range(1, 1025): response = os.system(f"nmap -p {port} {target_ip} -Pn | grep open") 
  # Use -Pn to assume host is online 
if response == 0: print(f"Port {port} is open") while True: target_ip = input("Enter the target IP address: ") 
# Ping the target to check if it's reachable ping_response = subprocess.call(["ping", "-c", "1", target_ip]) 

attributions bard.com
https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/
