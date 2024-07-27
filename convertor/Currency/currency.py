from os import system
import sys
import Currency.rates.exchange as exchange
import Currency.history.history as history
import Currency.available.available as available

def options():
    option = {1 : "Exchange Rates", 2: "Historical currency conversion", 3:"Available Rates", 4 : "Quit"}

    for key,i in enumerate(option.values()):
        print(f"{key+1}) {i}")

    try:
        selected_opt = int(input("\nEnter an number: "))
    except ValueError:
        print("Please enter a valid number.")
        
    if selected_opt in option:
        if selected_opt == 4:
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
    match opt:
        case "Exchange Rates":
            exchange.process()
        case "Available Rates":
            available.process()
        case "Historical currency conversion":
            history.process()