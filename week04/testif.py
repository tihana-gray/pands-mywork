# if condition1:
# statements(if true)
# elif condition2:
# statements(if condition is false but 2 is true)
# else:
# statements (if both conditions are false)

# Author: Tihana Gray

b = 1
if True:
    print("we are in the if statement")
    b = 22

c = 1
if c == 1:
    print ("c is one")
else:
    print ("c is not one")

d = 4
if d < 0:
    print("d is negative")
elif d > 10:
    print ("d is 10 or higher")
else:
    print("d is between 0 and 9 (inclusive)")

print("sanity ", b)

