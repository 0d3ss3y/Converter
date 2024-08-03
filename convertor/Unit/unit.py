import os
import sys
import requests

def options():
    option = {1:"Length", 
              2:"Weight", 
              3:"Volume", 
              4:"Temperature",
              5:"Area",
              6:"Time",
              7:"Quit"}
    
    codes = {
        "Length" : "len", 
        "Weight":"weight", 
        "Volume":"vol", 
        "Temperature":"temp",
        "Area":"area",
        "Time":"time"
    }

    for key,i in enumerate(option.values()):
        print(f"{key+1}) {i}")

    while True:
        try:
            selected_opt = int(input("\nEnter a number: "))

            if selected_opt in option:
                if selected_opt == 7:
                    print("Exiting....")
                    sys.exit()
                opt = option[selected_opt]
                return opt, codes[opt]
            else:
                print("Invalid option. Please choose a valid number")
        except ValueError:
            print("Please enter a valid number.")


def display_units(selected_category):
    units = {
        "length": ["mts", "kilomts", "cmts", "millimts", "micromts", "nanomts", "mile", "yard", "foot", "inch", "lightyear"],
        "weight": ["kgms", "gms", "mgms","pound", "ounce", "carrat"],
        "volume": ["lts", "mlts", "usgallon","uscup"],
        "temperature": ["celsius", "kelvin", "fahrenheit"],
        "area": ["sqmts","sqmile", "sqft", "acre", "hectare"],
        "time": ["sec", "milisec", "microsec", "nanosec", "picosec", "min", "hour", "day", "week", "month", "year"]
    }
    return units.get(selected_category, [])


def handleProcess(opt,code):
    url = 'http://127.0.0.1:5000/convert'
    
    # Display available units
    print(f"\nAvailable units for {opt}:")
    units = display_units(opt)
    print("Unit: ", ', '.join(units))
    
    while True:
        unit_from = input(f"\nEnter the unit you want to convert from ({opt}): ").strip()
        unit_to = input(f"Enter the unit you want to convert to ({opt}): ").strip()

        try:
            value = float(input("Enter the value: "))
            break
        except ValueError:
            print("Please enter a valid number")
            
    params = {
        'category' : code,
        'unit_from': unit_from,
        'unit_to' : unit_to,
        'value' : value
    }
    
    try:
        response = requests.get(url,params)
        response.raise_for_status()
        data = response.json()
        print(f"Converted Value: {value} = {data['result']}")
    except requests.RequestException as e:
        print(f"Error: {e}")
        print("Could not fetch the conversion result.")


def main():
    if os.name ==  "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

    opt,code = options()
    handleProcess(opt.lower(),code)
