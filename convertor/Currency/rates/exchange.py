import json
import os

file_path = "Currency/database/"

def process():
    initial_country_code, initial_country_name, initial_country_symbol = getInitial()
    target_country_code, target_name, target_symbol = getTarget()
    
    if not (initial_country_code and target_country_code):
        print("Conversion could not be completed due to invalid currency codes.")
        return
    
    try:
        amount = input(f"Enter amount in {initial_country_name} {initial_country_symbol}: ")
        amount_input = amount.replace(',', '.')
        amount = float(amount_input)  # Convert input to float
        final_amount = convert(amount, initial_country_code, target_country_code)
        
        if final_amount is not None:
            print(f"{initial_country_symbol} {amount:.2f} is equal to {target_symbol} {final_amount:.2f}")
        else:
            print("Conversion could not be completed due to an error.")
            
    except ValueError:
        print("Please enter a valid number.")

def getTarget():
    request = input("Please enter targeted country code: ").upper().strip()
    
    try:
        dir_path = os.path.join(file_path, 'currencies.json')

        if not os.path.exists(dir_path):
            raise FileNotFoundError("The 'currencies.json' file does not exist.")
        
        with open(dir_path, "r") as file:
            data = json.load(file)
            
            for currency_code, currency_info in data['data'].items():
                if request.lower() in currency_info.get('code', request).lower():
                    return currency_info['code'], currency_info["name"], currency_info["symbol"]
                
            print("Country not found in the database.")
            return None, None, None
    except FileNotFoundError as e:
        print(e)
    except json.JSONDecodeError:
        print("Error decoding JSON data from 'currencies.json'.")
    except Exception as e:
        print(f"Error reading currencies data: {e}")   
    
    return None, None, None

def getInitial():
    request = input("Please enter your country code: ")
    
    try:
        dir_path = os.path.join(file_path, 'currencies.json')

        if not os.path.exists(dir_path):
            raise FileNotFoundError("The 'currencies.json' file does not exist.")
        
        with open(dir_path, "r") as file:
            data = json.load(file)
            
            for currency_code, currency_info in data['data'].items():
                if request.lower() in currency_info.get('code', request).lower():
                    return currency_info['code'], currency_info["name"], currency_info["symbol"]
                
            print("Country not found in the database.")
            return None, None, None
    except FileNotFoundError as e:
        print(e)
    except json.JSONDecodeError:
        print("Error decoding JSON data from 'currencies.json'.")
    except Exception as e:
        print(f"Error reading currencies data: {e}")   
    
    return None, None, None

def convert(amount, currency_from, currency_to):
    try:
        json_path = os.path.join(file_path, "latest.json")
        
        if not os.path.exists(json_path):
            raise FileNotFoundError("The 'latest.json' file does not exist.")
        
        with open(json_path, "r") as file:
            data = json.load(file)
            from_rate = data['data'].get(currency_from, {}).get('value')
            to_rate = data['data'].get(currency_to, {}).get('value')
            
            if from_rate is None or to_rate is None:
                print("Currency code is not available in the database.")
                return None
            
            amount_in_usd = amount / from_rate
            final_amount = amount_in_usd * to_rate
            return final_amount
            
    except FileNotFoundError as e:
        print(e)
    except json.JSONDecodeError:
        print("Data decoding error.")
    except ZeroDivisionError:
        print("Error: Division by zero. Check the rates in 'latest.json'.")
    except Exception as e:
        print(f"Error during conversion: {e}")
    
    return None
