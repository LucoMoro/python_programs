from pathlib import Path

p = Path('ecommerce')
print(p.exists())
#print(p.mkdir()) to create the directory
#print(p.rmdir()) 
for file in p.glob('*.py'):
    print(file)