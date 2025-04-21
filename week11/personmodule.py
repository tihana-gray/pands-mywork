# demonstration of a module
# Author: Tihana Gray


import datetime as dt
def gethealthdata(person):
    print("get health data: ", person['firstname'])

def displayperson(person):
    print(person)

if __name__ == '__main__':
    person1 = {
        'firstname' : 'Tihana',
        'lastname' : 'Gray',
        'dob': dt.date(1983,9,22),
        'height': 168,
        'width' : 75
    }
    displayperson(person1)
    gethealthdata(person1)