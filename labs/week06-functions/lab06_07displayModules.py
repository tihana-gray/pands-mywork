# displaying modules
# Author: Tihana Gray

def displayModules(modules):
    print("\tName \tGrade")
    for module in modules:
        print(f"\t{module['name']} \t{module['grade']}") 
# error fixed by using single quotes inside the f-string

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])
