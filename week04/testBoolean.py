# messing with booleans
# booleans can be True or False
# boolean is the return type of the mathemarical operators
# = < > <= >= 
#
# flipped with the not keyword
# be careful using and or
#
# Author: Tihana Gray

is_alive = True
print (f"is_alive = {is_alive}")

var = (2 <= 4)
print (f"var = {var}")

logic = (2 <= 100) or (3 >= 100)
print (f"logic is {logic}")

grade = 400
logic = (grade < 0) or (grade > 100)
print (f"logic is {logic}")

grade = 40
invalid = (grade < 0) or (grade > 100)
print (f"invalid is {invalid}")
