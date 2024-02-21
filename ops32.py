import os
import hashlib
from datetime import datetime
  # Get file information
            file_size = os.path.getsize(file_path)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Print results
            print(f"Timestamp: {timestamp}")
            print(f"File Name: {file_name}")
            print(f"File Size: {file_size} bytes")
            print(f"MD5 Hash: {md5_hash}")
            print(f"File Path: {file_path}")
            print("-" * 50)
