# program that  that allows a user to create new students and to view students
# Author: Tihana Gray

def displayMenu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 
 return choice

#test the function
choice = displayMenu()
print(f"you chose { choice }")
