from pathlib import Path
from zipfile import ZipFile


#with ZipFile("files.zip", "w") as zip:
    #to zip a directory
    #for path in Path("ecommerce").rglob("*.*"):
        #zip.write(path)


with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("ecommerce/customer/contact.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")