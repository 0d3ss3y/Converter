# Data rate (bps to Kbps, Mbps to Gbps)
# WIFI Speed Test
# Password finder
# Phone Number
import os
import Device.Data.data as data
import Device.Info.info as dev_info
import Device.Number as phone
import Device.Wifi as network

options = {
    1 : "Info",
    2 : "WIFI",
    3 : "Phone Number",
    4 : "Data"
}

def clearing():
    os.system("cls" if os.name == 'nt' else "clear")

def determine_options():
    for key,option in options.items():
        print(f"{key} - {option}")
    
    try:
        selected_opt = int(input("\nEnter Option's Index: "))
        
        if selected_opt in options.keys():
            return(selected_opt)
            #return(options[selected_opt])
        else:
            main()
            
    except ValueError:
        print("Please a valid index") 
    
def main():
    clearing() 
    opt = determine_options()
    
    match (opt):
        case 1:
            dev_info.main()
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass