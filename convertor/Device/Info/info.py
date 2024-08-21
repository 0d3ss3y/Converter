import psutil
import os
import datetime
#CPU,Network,Memory

def clearing():
    os.system("cls" if os.name == 'nt' else "clear")

def cpu():
    #times = psutil.cpu_times(True)
    core_count = psutil.cpu_count(logical=True)
    usable_cores = len(psutil.Process().cpu_affinity())
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    boot_time = round(psutil.boot_time(),2)
    translated_time = datetime.datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")
    
    print("CPU STATS:")
    print(f"Number of cores: {core_count}\nUsable cores : {usable_cores}\n")
    
    print(f"Core Percentage Per Core:")
    for key,percent in enumerate(cpu_percent, start=1):
        print(f"Core {key} Percentage: {percent}")    
    print(f"\nBoot Time: {boot_time} seconds\nLast Booting time: {translated_time}") 
    
    
    
def main():
    clearing()
    cpu()
    