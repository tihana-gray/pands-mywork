# Program that stores a student name and a list of her courses and grades in a dict
# The program should then print out her data.
# The number of course she has could change.

# Author: Tihana Gray

'''
student = {
"name":"Mary",
"modules": [
    {
        "courseName":"Programming",
        "grade": 45
    },
    {
        "courseName":"History",
        "grade":99
    }
]
}
print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))

'''
# program that will read in the data for the data structure above
# ie reads in a student’s name, then keeps reading in their modules and grades
# (until the user enters a blank module name)
'''
student = {}
student["name"] = input("Enter student name: ")
student["modules"] = []

while True:
    course_name = input("Enter course name (or press Enter to finish): ")
    if course_name == "":
        break  # Exit loop if input is blank

    grade = int(input(f"Enter grade for {course_name}: "))  # Read grade
    student["modules"].append({"courseName": course_name, "grade": grade})

# Print student data
print(f"\nStudent: {student['name']}")
for module in student["modules"]:
    print(f"\t {module['courseName']} \t: {module['grade']}")
'''

# read in multiple students (until the student_name is blank)

students = []  # List to store multiple students

while True:
    student_name = input("Enter student name (or press Enter to finish): ")
    if student_name == "":
        break  # when a blank name is entered

    student = {"name": student_name, "modules": []}

    while True:
        course_name = input("Enter course name (or press Enter to finish): ")
        if course_name == "":
            break  # when a blank course name is entered

        grade = int(input(f"Enter grade for {course_name}: "))  
        student["modules"].append({"courseName": course_name, "grade": grade})

    students.append(student)  # Store the student's data

# Print all students' data
print("\nStudent Records:")
for student in students:
    print(f"Student: {student['name']}")
    for module in student["modules"]:
        print(f"\t {module['courseName']} \t: {module['grade']}")
    print()  
