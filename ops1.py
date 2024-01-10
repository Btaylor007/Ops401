import os
import platform
import subprocess
import time
from datetime import datetime

def ping(host):
    """Check network connectivity to a host using a single ICMP packet."""
    operating_system = platform.system().lower()
    param = "-n" if operating_system == "windows" else "-c"
    command = ['ping', param, '1', host]

    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        return True
    except subprocess.CalledProcessError:
        return False

def uptime_sensor(ip):
    """Continuously monitors the network connectivity to a specified IP address."""
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Truncate milliseconds to microseconds
        status = "Network Status Active" if ping(ip) else "Network Status Inactive"
        print(f"{timestamp} {status} to {ip}")
        time.sleep(2)

if __name__ == "__main__":
    target_ip = input("Enter IP address: ")  # Prompt for IP address
    uptime_sensor(target_ip)

attributions chatGPT and Bard
