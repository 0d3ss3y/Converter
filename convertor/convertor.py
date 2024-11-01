import Currency.currency as cur
import File.file as file
import Unit.unit as unit
import Device.device as dev
import os

def starting():
    options =  ["Currency","Electrical","File","Financial","Gaming","Health"
                ,"Language","Device","Time","Unit","Url"]

    print("Convertor Menu:\n")
    for key,opt in enumerate(options):
        print(f"{key+1}) {opt}")
    print("To quit enter 'q' or 'quit'")


    while True:
        selected_opt = input("\nEnter an option: ").capitalize()

        if selected_opt in options:
            ProcessOpt(selected_opt)
            break
        elif selected_opt in ["Quit","Q"]:
            break
        else:
            print("Invalid option. Please try again.")
            

def clearing():
    os.system("cls" if os.name == 'nt' else "clear") 
            
def ProcessOpt(opt):
    print(opt)
    clearing()
    match opt:
        case "Currency":
            cur.main()
 
        case "Electrical":
            print("You selected Electrical")
            # Add your electrical processing code here
        case "File":
            file.main()
            # Add your file processing code here
        case "Financial":
            print("You selected Financial")
            # Add your financial processing code here
        case "Gaming":
            print("You selected Gaming")
            # Add your gaming processing code here
        case "Health":
            print("You selected Health")
            # Add your health processing code here
        case "Language":
            print("You selected Language")
            # Add your language processing code here
        case "Device":
            dev.main()
        case "Programming":
            print("You selected Programming")
            # Add your programming processing code here
        case "Time":
            print("You selected Time")
            # Add your time processing code here
        case "Unit":
            unit.main()
        case "Url":
            print("You selected URL")
            # Add your URL processing code here
        case _:
            print("Unhandled option")


if __name__ == "__main__":
    starting()