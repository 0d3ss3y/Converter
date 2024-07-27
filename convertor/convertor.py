import Currency.currency as cur

def starting():
    options =  ["Currency","Data","Electrical","File","Financial","Gaming","Health"
                ,"Language","Measurement","Network","Programming","Time","Unit","Url"]

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
            

def ProcessOpt(opt):
    print(opt)
    match opt:
        case "Currency":
            print("You selected Currency")
            cur.main()
            # Add your currency processing code here
        case "Data":
            print("You selected Data")
            # Add your data processing code here
        case "Electrical":
            print("You selected Electrical")
            # Add your electrical processing code here
        case "File":
            print("You selected File")
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
        case "Measurement":
            print("You selected Measurement")
            # Add your measurement processing code here
        case "Network":
            print("You selected Network")
            # Add your network processing code here
        case "Programming":
            print("You selected Programming")
            # Add your programming processing code here
        case "Time":
            print("You selected Time")
            # Add your time processing code here
        case "Unit":
            print("You selected Unit")
            # Add your unit processing code here
        case "Url":
            print("You selected URL")
            # Add your URL processing code here
        case _:
            print("Unhandled option")



if __name__ == "__main__":
    starting()