from datetime import datetime
import os
import json
import currencyapicom

file_path = "Currency/database/"

def process():
    date = determineDate()
    #saveHistory(date)
    target_country_code, target_symbol, meta = determineCountry()
       
    
def saveHistory(date):        
    try:
        client = currencyapicom.Client("cur_live_4ZC94me0yoNBhtbf4zelEMhwb16MB9qJzrzOj3eB")
        data = client.historical(date)

        os.makedirs(file_path, exist_ok=True)
        dir_path = os.path.join(file_path, 'history.json')

        with open(dir_path, "w") as file:
            json.dump(data, file, indent=4)
    except json.JSONDecodeError:
        print("Error decoding JSON data for latest rates.")
    except Exception as e:
        print(f"Error saving latest data: {e}")
  
    
def determineCountry():
    request = input("Please enter targeted country code: ").upper().strip()
    
    try:
        dir_path = os.path.join(file_path, 'history.json')

        if not os.path.exists(dir_path):
            raise FileNotFoundError("The 'history.json' file does not exist.")
        
        with open(dir_path, "r") as file:
            data = json.load(file)
            
            for currency_code, currency_info in data['data'].items():
                meta = data['meta'].get('last_updated_at')
                if request.lower() in currency_info.get('code', request).lower():
                    return currency_info['code'], currency_info["value"],meta
                
            print("Country not found in the database.")
            return None, None, None
    except FileNotFoundError as e:
        print(e)
    except json.JSONDecodeError:
        print("Error decoding JSON data from 'currencies.json'.")
    except Exception as e:
        print(f"Error reading currencies data: {e}")   
    
    return None, None, None


def determineDate():
    # Date to retrieve historical rates from (format: 2021-12-31)
    date_input = input("Enter your preferred date (YYYY-MM-DD): ")

    try:
        date = datetime.strptime(date_input, '%Y-%m-%d')
        iso_date = date.isoformat()
        return iso_date
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return None


def display(code,symbol,meta):
    os.system('cls')
    print(f"")