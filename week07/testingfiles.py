# testing my directory and file access

import os

file_path = r"C:\Users\tihan\OneDrive\Desktop\ATU\pands\pands-mywork\week07\messingwithfiles.py"

print("Current working directory:", os.getcwd())
print("Looking for:", file_path)

print("\nFiles in directory:")
for f in os.listdir(r"C:\Users\tihan\OneDrive\Desktop\ATU\pands\pands-mywork"):
    print("-", f)

print("\nFile exists:", os.path.exists(file_path))
