import os

file_path = "qwe.txt"

if os.path.exists(file_path) and os.access(file_path, os.W_OK):
    os.remove(file_path)
    print("File deleted")
else:
    print("File not found or no access")
