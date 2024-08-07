import os

def clearing(): 
    os.system("cls" if os.name == 'nt' else "clear")

def main():
    clearing()
    # # Prompt user to drag and drop files into the terminal
    # print("Drag and drop the files into this terminal window and press Enter:")
    
    # # Read input from the user
    # pdf_location = input("File paths: ")    
    # pdf_name = pdf_location.strip().split("\\")
    # print(f"Name : {pdf_name[-1]}")
    opt = options()
    print(opt)
    
    match opt:
        case "Image":
            pass
        case "Document":
            pass
        case "Audio":
            pass
        case "Video":
            pass
        
        
    
def options():
    option_list = {1:"Image",
                   2:"Document",
                   3:"Audio",
                   4:"Video"}
    
    while True:
        clearing()

        for key,value in option_list.items():
            print(f"{key}) {value}")
            
        try:
            opt = int(input("Enter an index: "))
        
            if opt not in option_list.keys():
                print("Invalid Option")
                continue
            return(option_list[opt])
            
            
        except(ValueError):
            print("Enter a valid index")
        
        