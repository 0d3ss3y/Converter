import psutil

def cpu_count():
    cpu_percentage = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq(True)
    
    print("CPU Usuage per core:")
    print(f"Number of cores : {cpu_percentage}")
    
    for information in cpu_freq:
        print(information)
    #print(cpu_freq)

    
    
def main():
    cpu_count()
    