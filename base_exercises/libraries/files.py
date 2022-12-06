from pathlib import Path
#to print a human readible time
from time import ctime
import shutil


#path = Path("ecommerce/customer/contact.py")
#path.exists()
#path.rename("init.txt")
#path.unlink()
#print(ctime(path.stat().st_ctime))

#path.read_bytes() reading bytes froma a file
#print(path.read_text()) returns the content of the file as a string

#open function
#with open("ecommerce/customer/contact.py", "r") as file:
#    pass

#print(path.read_text())

#path.write_bytes()
#path.write_text("...")

source = Path("ecommerce/customer/contact.py")
target = Path() / "__init__.py"

#bad away
target.write_text(source.read_text())

#easier and cleaner way
shutil.copy(source, target)