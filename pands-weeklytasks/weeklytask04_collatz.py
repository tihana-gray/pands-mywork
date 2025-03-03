# Program that asks the user to input any positive integer and outputs 
# the successive values of the following calculation:
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# The program should end if the current value is one.

# Author: Tihana Gray

def collatz(n):
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    print(n)  # Print the final 1

# Get user input
try:
    num = int(input("Enter a positive integer: "))
    if num > 0:
        collatz(num)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")