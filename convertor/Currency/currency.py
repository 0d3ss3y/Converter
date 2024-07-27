import os
import json
import currencyapicom
import sys
import Currency.rates.exchange as exchange
import Currency.history.history as history
import Currency.available.available as available

file_path = "Currency/database"


def updateJson():
    try:
        client = currencyapicom.Client("cur_live_4ZC94me0yoNBhtbf4zelEMhwb16MB9qJzrzOj3eB")
        #currency_json = client.currencies()
        latest_json = client.latest()

        #saveCurrencies(currency_json)
        saveLatest(latest_json)
    except Exception as e:
        print(f"Error updating JSON: {e}")
       
    
def saveLatest(data):
    try:
        os.makedirs(file_path, exist_ok=True)
        dir_path = os.path.join(file_path, 'latest.json')

        with open(dir_path, "w") as file:
            json.dump(data, file, indent=4)
    except json.JSONDecodeError:
        print("Error decoding JSON data for latest rates.")
    except Exception as e:
        print(f"Error saving latest data: {e}")
    
        
def saveCurrencies(data):
    try:
        os.makedirs(file_path, exist_ok=True)
        dir_path = os.path.join(file_path, 'currencies.json')

        with open(dir_path, "w") as file:
            json.dump(data, file, indent=4)
    except json.JSONDecodeError:
        print("Error decoding JSON data for currencies.")
    except Exception as e:
        print(f"Error saving currencies data: {e}")


def options():
    option = {1 : "Exchange Rates", 2: "Historical currency conversion", 3:"Available Rates", 4 : "Quit"}

    for key,i in enumerate(option.values()):
        print(f"{key+1}) {i}")

    while True:
        try:
            selected_opt = int(input("\nEnter a number: "))
            if selected_opt in option:
                if selected_opt == 4:
                    print("Exiting...")
                    sys.exit()
                return option[selected_opt]
            else:
                print("Invalid option. Please choose a valid number.")
        except ValueError:
            print("Please enter a valid number.")


def handleProcess(opt):
    match opt:
        case "Exchange Rates":
            exchange.process()
        case "Available Rates":
            available.process()
        case "Historical currency conversion":
            history.process()
            

def main():
    if os.name == 'posix':
        os.system("clear")
    elif os.name == 'nt':
        os.system("cls")
        
    updateJson()
    opt = options()
    handleProcess(opt)