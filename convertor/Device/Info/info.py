import psutil

def cpu_count():
    cpu_percentage = psutil.cpu_count(1,True)
    cpu_freq = psutil.cpu_freq(True)
    
    print("CPU Usuage per core:")
    for i,(percent,freq) in enumerate(zip(cpu_percentage,cpu_freq),start=1):
        print(f"Core {i}: {percent}% \nFrequency : {freq.current} MHz")
    
def main():
    cpu_count()
    