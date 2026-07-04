import psutil
import time

def check_system():
    print(f"--- System Monitor ---")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"RAM Usage: {psutil.virtual_memory().percent}%")

if __name__ == "__main__":
    check_system()
