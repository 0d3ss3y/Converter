# Data rate (bps to Kbps, Mbps to Gbps)
# WIFI Speed Test
# Password finder
# Phone Number
import os

options = {
    1 : "Info",
    2 : "WIFI",
    3 : "Phone Number"
}


def clearing():
    os.system("cls" if os.name == 'nt' else "clear")

def determine_options():
    for key,option in options.items():
        print(f"{key} - {option}")
    
    try:
        selected_opt = int(input("Enter Option's Index: "))
        
        if selected_opt in options.keys():
            return(selected_opt)
        else:
            main()
            
    except ValueError:
        print("Please a valid index") 
    
    
def main():
    clearing() 
    opt = determine_options()