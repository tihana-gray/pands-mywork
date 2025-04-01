# flow control if elif and else
# program that asks the user ro enter in a number, and the program will tell the user if the number is even or odd.

# Author: Tihana Gray

number = int(input("Enter an integer: "))
if (number % 2) == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")