# messsing with the os module
# Author: Tihana Gray

import os

file_path = r"C:\Users\tihan\OneDrive\Desktop\ATU\pands\pands-mywork\week07\messingwithfiles.py"

FILENAME = "messingwithfiles.py"


if os.path.exists(file_path):
    with open(file_path, "r") as f:
        for line in f:
            print(line, end='')
else:
    print(file_path, "does not exist")

os.remove("data2.txt")

