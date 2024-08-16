import requests

def main(category,to_ext,dir_in,name):
    url = 'http://127.0.0.1:5000/convert'
    
    params = {
        'category' : category,
        'name': name,
        'to' : to_ext,
        'pathway' : dir_in
    }
    
    try:
        response = requests.get(url,params)
        response.raise_for_status()
        data = response.json()
        print(f"Successfully converted\nCheck your download folder")
    except requests.RequestException as e:
        print(f"Error: {e}")
        print("Could not fetch the conversion result.")
