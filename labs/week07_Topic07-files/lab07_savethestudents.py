# learning the doSave[] function
# Author: Tihana Gray

import json
import os.path

FILENAME = "studentData.json"
students = []

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(l) Load students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/l/q): ").strip()
    return choice

def doAdd(students):
    name = input("Enter student name: ")
    student = {}
    student["name"] = name
    students.append(student)
    print(f"Added student: {name}")

def doView(students):
    if not students:
        print("No students to view.")
    for student in students:
        print(f"Name: {student['name']}")

def writeDict(dictToSave):
    with open(FILENAME, "wt") as f:
        json.dump(dictToSave, f)

def readDict():
    if not os.path.isfile(FILENAME):
        print("No data file found. Starting with an empty list.")
        return []
    with open(FILENAME, "rt") as f:
        return json.load(f)

def doSave(students):
    writeDict(students)
    print("Students saved.")

def doLoad():
    return readDict()

# main program loop
choice = displayMenu()
while choice != 'q':
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave(students)
    elif choice == 'l':
        students = doLoad()
        print("Students loaded.")
    else:
        print("\n\nPlease select either a, v, s, l or q")

    choice = displayMenu()

print("Goodbye!")
