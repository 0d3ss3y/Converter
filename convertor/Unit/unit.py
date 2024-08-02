import os
import sys
import Unit.conversion.conversion as convert

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


def handleProcess(opt,code):
    convert.process(opt,code)


def main():
    if os.name ==  "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

    opt,code = options()
    handleProcess(opt.lower(),code)
