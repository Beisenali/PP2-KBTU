import os

path = "qwe.txt"

if os.path.exists(path):
    print("File name:", os.path.basename(path))  
    print("Folder:", os.path.dirname(path))  
else:
    print("The path doesn't exist")
