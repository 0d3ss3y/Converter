from os import system
import sys

def options():
    option = {1 : "Exchange Rates", 2: "Historical currency conversion", 3 : "Quit"}

    for key,i in enumerate(option.values()):
        print(f"{key+1}) {i}")

    while True:
        try:
            selected_opt = int(input("\nEnter an number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if selected_opt in option:
            if selected_opt == 3:
                print("Exiting...")
                sys.exit()
            return option[selected_opt]
        else:
            print("Invalid option. Please choose a valid number.")


def main():
    system("clear")
    opt = options()
    handleProcess(opt)


def handleProcess(opt):
    pass