#!/usr/bin/env python3
import os
import sys
import time
import psutil
from datetime import datetime

def get_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024
    return f"{bytes:.1f} PB"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_bar(percent, width=20):
    filled = int(width * percent / 100)
    empty = width - filled
    return '█' * filled + '░' * empty

def main():
    print("\033[92m" + "="*60)
    print("         SYSTEM RESOURCE MONITOR")
    print("="*60 + "\033[0m")
    
    try:
        while True:
            clear()
            
            print("\033[97m" + "="*60)
            print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("="*60 + "\033[0m")
            
            cpu_percent = psutil.cpu_percent(interval=0.5)
            if cpu_percent < 50:
                cpu_color = '\033[92m'
            elif cpu_percent < 80:
                cpu_color = '\033[93m'
            else:
                cpu_color = '\033[91m'
            
            print(f"\n\033[97mCPU:\033[0m {cpu_color}{cpu_percent:5.1f}% {get_bar(cpu_percent)} \033[0m")
            
            ram = psutil.virtual_memory()
            if ram.percent < 50:
                ram_color = '\033[92m'
            elif ram.percent < 80:
                ram_color = '\033[93m'
            else:
                ram_color = '\033[91m'
            
            print(f"\n\033[97mRAM:\033[0m {ram_color}{ram.percent:5.1f}% {get_bar(ram.percent)} \033[0m")
            print(f"     Used: {get_size(ram.used)} / Total: {get_size(ram.total)}")
            
            disk = psutil.disk_usage('/')
            if disk.percent < 50:
                disk_color = '\033[92m'
            elif disk.percent < 80:
                disk_color = '\033[93m'
            else:
                disk_color = '\033[91m'
            
            print(f"\n\033[97mDISK:\033[0m {disk_color}{disk.percent:5.1f}% {get_bar(disk.percent)} \033[0m")
            print(f"     Used: {get_size(disk.used)} / Total: {get_size(disk.total)}")
            
            net = psutil.net_io_counters()
            print(f"\n\033[97mNETWORK:\033[0m")
            print(f"     Sent: {get_size(net.bytes_sent)}")
            print(f"     Recv: {get_size(net.bytes_recv)}")
            
            print("\n\033[90m" + "-"*60)
            print("Press Ctrl+C to exit")
            print("-"*60 + "\033[0m")
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\033[92mGoodbye!\033[0m")
        sys.exit(0)

if __name__ == "__main__":
    try:
        import psutil
    except ImportError:
        print("Installing psutil...")
        os.system("pip install psutil")
        import psutil
    
    main()