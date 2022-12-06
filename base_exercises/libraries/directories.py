from pathlib import Path

path = Path("ecommerce")
path.exists()
#path.mkdir() create the directoty
#path.rmdir() remove the directoty
#path.rename("ecommerce2") remove the directoty

#print(path.iterdir()) 

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob("**/*.py")] #glob("**/*.py") to search recusrively, or use rglob("*.py")
#print(paths)
print(py_files)