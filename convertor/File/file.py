import os
from pdf2docx import parse

def clearing(): 
    os.system("cls" if os.name == 'nt' else "clear")

def main():
    clearing()
    loc,name, ext = process()
    
def process():
    # Prompt user to drag and drop files into the terminal
    print("Drag and drop the files into this terminal window and press Enter:")
    
    # Read input from the user
    pdf_location = input("File paths: ")    
    pdf_name = pdf_location.strip().split("\\")
    ext_type = pdf_name[-1].split(".")[1]
    ext = ext_type.upper().replace('"'," ").strip()
    clearing()
    print(f"Name : {pdf_name[-1]}")
    print(f"Extension: {ext}")
    #print(f"Extension: {ext_type.upper().replace('"'," ").strip()}")
    return pdf_location,pdf_name,ext