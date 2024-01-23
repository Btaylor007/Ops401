#!/usr/bin/env python3


from scapy.all import *

def tcp_port_scanner(host, port_range):
    for port in range(port_range[0], port_range[1] + 1):
        # Crafting a TCP SYN packet
        packet = IP(dst=host) / TCP(dport=port, flags="S")
        
        # Sending the packet and receiving the response
        response = sr1(packet, timeout=1, verbose=0)

        if response:
            # Checking the TCP flags in the response
            if response.haslayer(TCP):
                flags = response[TCP].flags

                # If SYN-ACK (flags=0x12) is received, send a RST packet and notify the user
                if flags == 0x12:
                    rst_packet = IP(dst=host) / TCP(dport=port, flags="R")
                    send(rst_packet, verbose=0)
                    print(f"Port {port} is open")

                # If RST (flags=0x14) is received, notify the user the port is closed
                elif flags == 0x14:
                    print(f"Port {port} is closed")

            # If no TCP layer is found, consider the port as filtered and silently dropped
            else:
                print(f"Port {port} is filtered (no response)")

        # If no response is received, consider the port as filtered and silently dropped
        else:
            print(f"Port {port} is filtered (no response)")

if __name__ == "__main__":
    # Define the host IP and port range
    target_host = "127.0.0.1"
    target_port_range = (1, 100)  # Example: Scan ports from 1 to 100

    # Run the TCP port scanner
    tcp_port_scanner(target_host, target_port_range)

#ATTRBUTUIONS CHATGPT https://www.freecodecamp.org/news/how-to-use-scapy-python-networking/ https://python.plainenglish.io/python-basics-packet-crafting-with-scapy-b3e4ea5c8111
