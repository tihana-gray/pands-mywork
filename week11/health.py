# use person module
# Author: Tihana Gray

from personmodule import *
import datetime as dt

person1 = {
    'firstname': 'Tihana',
    'lastname': 'Gray',
    'dob': dt.date(1983, 9, 22),
    'height': 168,
    'width': 75
}

# call the functions in the module
# I used import * so these have been imported
# so I can call them with out the module name
displayperson(person1)
gethealthdata(person1)