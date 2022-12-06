from pathlib import Path

#Path(r"C:\ProgramFiles\Microsoft") r to avoid \\
#Path("ecommerce/__init__.py")
#Path() / "ecommerce" / "__init.py__" combining strings
#Path.home() returns the home directory of the current user

path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem) #returns the file whitout the extenction
print(path.suffix)
print(path.parent)
#path = path.with_name("file.txt")
#print(path)
#print(path.absolute()) #prints the absolute path of "file.txt"
path = path.with_suffix(".txt")
print(path)