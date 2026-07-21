import os
import time
import hashlib
from datetime import datetime

# ==============================
# Configuration
# ==============================

WATCH_DIRECTORY = input("Enter folder path to monitor: ").strip()
CHECK_INTERVAL = 5

# ==============================
# Hash Function
# ==============================

def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    try:
        with open(filepath, "rb") as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()

    except:
        return None


# ==============================
# Initial Scan
# ==============================

def scan_directory(path):

    file_hashes = {}

    for root, dirs, files in os.walk(path):

        for file in files:

            full_path = os.path.join(root, file)

            file_hashes[full_path] = calculate_hash(full_path)

    return file_hashes


# ==============================
# Logging
# ==============================

def log(message):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    text = f"[{now}] {message}"

    print(text)

    with open("ids_log.txt", "a") as f:
        f.write(text + "\n")


# ==============================
# Monitor
# ==============================

def monitor():

    print("\nScanning files...")

    previous = scan_directory(WATCH_DIRECTORY)

    print("Monitoring Started...\n")

    while True:

        time.sleep(CHECK_INTERVAL)

        current = scan_directory(WATCH_DIRECTORY)

        # New Files

        for file in current:

            if file not in previous:

                log(f"[+] New File Created : {file}")

        # Deleted Files

        for file in previous:

            if file not in current:

                log(f"[-] File Deleted : {file}")

        # Modified Files

        for file in current:

            if file in previous:

                if current[file] != previous[file]:

                    log(f"[!] File Modified : {file}")

        previous = current


# ==============================

if __name__ == "__main__":

    if not os.path.exists(WATCH_DIRECTORY):

        print("Folder not found.")

    else:

        monitor()
