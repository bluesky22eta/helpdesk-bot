import subprocess
import platform

def run():
    print("\n--- Restarting Network Adapter ---")
    if platform.system().lower() != "windows":
        print("❌ This feature is only supported on Windows.")
        return

    try:
        subprocess.run(["powershell", "-Command",
                        "Get-NetAdapter | Restart-NetAdapter -Confirm:$false"],
                        check=True)
        print("✅ Network adapter restarted.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to restart network adapter: {e}")
