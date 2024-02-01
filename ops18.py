#!/usr/bin/env python3


# import modules
import ssl
import time
import paramiko
import getpass
from zipfile import ZipFile

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# define functions for modes
def dict_it(target_file):
    try:
        # open file, read, and save to mem as 'file'
        with open(target_file, 'r') as file:
            # iterate through word list
            for word in file:
                # remove any leading/ending characters
                word = word.strip()
                print(word)
                # 2 second delay between words
                time.sleep(2)
    except FileNotFoundError:
        print("Please check the file path and try again.")

def pass_rec(user_word, target_file):
    try:
        with open(target_file, 'r') as file:
            if user_word in (word.strip().lower() for word in file):
                print(f"The word '{user_word}' is in the word list.")
            else:
                print(f"The word {user_word} is not in the word list.")
    except FileNotFoundError:
        print("That is not a valide file path.")

def get_host():
    host = input("Please enter an SSH Client to connect to or enter for default: ") or "127.0.0.1"
    return host

def get_user():
    user = input("Please enter a username or enter for default: ") or "user1"
    return user

def get_password():
    password = input("Please enter a password or enter for default: ") or "password1234"
    return password

def ssh_endpoint():
    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(get_host(), port, get_user(), get_password())
        stdin, stdout, stderr = ssh.exec_command("whoami")
        time.sleep(2)
        output = stdout.read()
        print("-" * 80)
        print(output)
        stdin, stdout, stderr = ssh.exec_command("ls -l")
        time.sleep(2)
        output = stdout.read()
        print(output)
      Attributions 
Tommy Taylor 
