import json
import os

file_path = "Currency/database"

def process():
    ask = getRequest()
    getCountry(ask)


def getRequest():
    try:
        request = input("Please enter desired country: ")
        return request
    except ValueError:
        print("Please Enter A String Value")
    

def getCountry(country):
    try:
        os.makedirs(file_path, exist_ok=True)
        dir_path = os.path.join(file_path, 'latest.json')

        with open(dir_path, "r") as file:
            data = json.load(file)
            
            for currency_code, currency_info in data['data'].items():
                
                if country in currency_info['name']:
                    print(f"\nCurrency Code: {currency_code}")
                    print(f"Symbol: {currency_info['symbol']}")
                    print(f"Name: {currency_info['name']}")
                    print(f"Native Symbol: {currency_info['symbol_native']}")
                    print(f"Decimal Digits: {currency_info['decimal_digits']}")
                    print(f"Rounding: {currency_info['rounding']}")
                    print(f"Code: {currency_info['code']}")
                    print(f"Plural Name: {currency_info['name_plural']}")
                    print(f"Type: {currency_info['type']}")
                    print(f"Countries: {', '.join(currency_info['countries'])}")
                    print()  
                    return currency_info['code']
                else:
                    continue
    except FileNotFoundError:
        print("The 'currencies.json' file does not exist.")
    except json.JSONDecodeError:
        print("Error decoding JSON data from 'currencies.json'.")
    except Exception as e:
        print(f"Error reading currencies data: {e}")   
    
    return


def read():
    try:
        os.makedirs(file_path, exist_ok=True)
        dir_path = os.path.join(file_path, 'latest.json')

        with open(dir_path, "r") as file:
            data = json.load(file)
            
            for currency_code, currency_info in data['data'].items():
                print(f"Currency Code: {currency_code}")
                print(f"Symbol: {currency_info['symbol']}")
                print(f"Name: {currency_info['name']}")
                print(f"Native Symbol: {currency_info['symbol_native']}")
                print(f"Decimal Digits: {currency_info['decimal_digits']}")
                print(f"Rounding: {currency_info['rounding']}")
                print(f"Code: {currency_info['code']}")
                print(f"Plural Name: {currency_info['name_plural']}")
                print(f"Type: {currency_info['type']}")
                print(f"Countries: {', '.join(currency_info['countries'])}")
                print()  
    except FileNotFoundError:
        print("The 'currencies.json' file does not exist.")
    except json.JSONDecodeError:
        print("Error decoding JSON data from 'currencies.json'.")
    except Exception as e:
        print(f"Error reading currencies data: {e}")     