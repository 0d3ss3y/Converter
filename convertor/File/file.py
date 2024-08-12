import os

def clearing(): 
    os.system("cls" if os.name == 'nt' else "clear")

def main():
    clearing()
    loc,name, ext = process()
    
def process():
    print("Drag and drop the files into this terminal window and press Enter:")
    pdf_location = input("File paths: ").strip()
    pdf_location = pdf_location.strip("'\"")
    pdf_name_parts = pdf_location.split("/")
    file_name = pdf_name_parts[-1].strip("'\"")  # Strip surrounding quotes from the file name
    
    ext_type = file_name.split(".")
    if len(ext_type) > 1:
        ext = ext_type[-1].upper().strip("'\"")  # Strip surrounding quotes from the extension
    else:
        ext = ""
    
    print(f"Name : {file_name}")
    print(f"Extension: {ext}")
    
    return pdf_location, file_name, ext
