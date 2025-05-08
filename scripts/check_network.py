import socket
import subprocess
import platform

def is_connected():
    try:
        # Ping Google DNS
        host = "8.8.8.8"
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "1", host]
        subprocess.check_output(command, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def get_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except:
        return "Could not determine IP."

def run():
    print("\n--- Network Check ---")
    if is_connected():
        print("✅ Internet connection is active.")
    else:
        print("❌ No internet connection detected.")
    
    print(f"📡 Local IP Address: {get_ip()}")
