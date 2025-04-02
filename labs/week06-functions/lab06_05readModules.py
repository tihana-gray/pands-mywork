# program that keeps reading modules until the user enters a module name or blank
# Author: Tihana Gray

students = []

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit): ").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit): ").strip()

    return modules

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

# test
doAdd(students)
doAdd(students)
print(students)

