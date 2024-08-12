import os
import requests

allowed_ext = {"Image" :["JPEG","PNG", "BMP","GIF","JPG"],
               "Document" :["PDF","DOCX"],
               "AUDIO" :["M4A","MP3","WAV"],
               "VIDEO" :["MP4","AVI"]}

def process(opt):
    for key,values in allowed_ext.items():
        if opt in values:
            return display_opt(key,values,opt)
        else:
            print("Unknown Extension")
    return False


def check_opt(opt,values):
    if opt in values:
        return True
    return False


def display_opt(title,values,opt):
        os.system("cls" if os.name == 'nt' else "clear")

        print(f"{title} Options:")

        for value in (values):
            if value == opt:
                continue
            else:
                print(f"- {value}")

        selected_opt = input("\nSelect an conversion option: ").upper()
        return check_opt(selected_opt,values)
