#breanna taylor 
#02/12/2024


import os
import logging
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(filename='encryption_tool.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_key():
    return Fernet.generate_key()

def save_key(key, key_file):
    with open(key_file, 'wb') as file:
        file.write(key)

def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

def encrypt_file(key, file_path):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(key, file_path):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def encrypt_folder(key, folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if not file_path.endswith('.encrypted'):
                encrypt_file(key, file_path)

def decrypt_folder(key, folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.encrypted'):
                decrypt_file(key, file_path)

if __name__ == "__main__":
    key_file = 'encryption_key.key'
    folder_to_encrypt = 'path/to/your/folder'
    folder_to_decrypt = 'path/to/your/encrypted/folder'

    # Configure logging to write logs to a file
    try:
        key = generate_key()
        save_key(key, key_file)
        logging.info('Encryption key generated and saved successfully.')
    except Exception as e:
        logging.error(f'Error generating or saving encryption key: {e}')

    # Encrypt folder with error handling
 
        

    # Decrypt folder with error handling
  
     #attributions chatgpt,https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux/,https://dotnettutorials.net/lesson/logging-module-in-python/
