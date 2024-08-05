import os

def main():
    os.system("cls" if os.name == 'nt' else "clear")
    
    # Prompt user to drag and drop files into the terminal
    print("Drag and drop the files into this terminal window and press Enter:")
    
    # Read input from the user
    pdf_location = input("File paths: ")    
    pdf_name = pdf_location.strip().split("\\")
    print(f"Name : {pdf_name[-1]}")
    opt = options()
    
def options():
    os.system("cls" if os.name == 'nt' else "clear")
    option_list = {1:"Image",
                   2:"Document",
                   3:"Audio",
                   4:"Video"}