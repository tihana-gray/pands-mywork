# This program reads in
# a students percentage
# and prints out the
# corresponding grade

# Author: Tihana Gray

percentage = float(input("Enter the percentage: "))
# print (percentage)

# be careful with ands and ors
if percentage < 0 or percentage > 100:
    # Later we will show you error handling
    # This should really throw an error
    print ("Please enter a number between 0 and 100")
elif percentage < 40: # we know it is greater than 0
    print ("Fail")
elif percentage < 50: # between 40 and 49
    print ("Pass")
elif percentage < 60: # between 50 and 59
    print ("Merit1")    
elif percentage < 70: # between 60 and 69
    print ("Merit2")
else: # the only option left is between 70 and 100
    print ("Distinction")

# Extra: In practice the percentages are rounded ie 69.5 gets rounded to 70 so is
# equal to a Distinction.
# Modifying the program to deal with this.

# This program keeps asking for a percentage until the user enters -1

while True:
    percentage = float(input("Enter the percentage (-1 to exit): "))
    
    if percentage == -1:
        print("Exiting program...")
        break  # Exit the loop if the user enters -1

    percentage = round(percentage)  # Round the percentage before checking

    if percentage < 0 or percentage > 100:
        print("Please enter a number between 0 and 100")
    elif percentage < 40:  
        print("Fail")
    elif percentage < 50:  
        print("Pass")
    elif percentage < 60:  
        print("Merit2")  
    elif percentage < 70:  
        print("Merit1")  
    else:  
        print("Distinction")