import os
import File.Saver.saver as save
import File.Saver.convertor as convert

def clearing(): 
    os.system("cls" if os.name == 'nt' else "clear")

def main():
    clearing()
    loc,name, ext = process()
    clearing()
    print(f"Name : {name}")
    print(f"Extension: {ext}\n")

    check,target_ext = save.process(ext)
    clearing()
        
    if check and target_ext != None:
        print(f"Converting {name} to {target_ext}")
    else:
        print(f"Can't convert")
    
def process():
    print("Drag and drop the files into this terminal window and press Enter:")
    
    pdf_location = input("File paths: ").strip()
    
    pdf_location = pdf_location.strip("'\"")
    
    pdf_name_parts = pdf_location.split("/")
    file_name = pdf_name_parts[-1].strip("'\"") 
    print(file_name)
    ext_type = file_name.split(".")
    name = file_name.split(".")[0]

    if len(ext_type) > 1:
        ext = ext_type[-1].upper().strip("'\"")  
    else:
        ext = ""
    
    return pdf_location, name, ext
