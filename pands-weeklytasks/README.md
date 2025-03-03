# Programming and Scripting: My Weekly Tasks

by Tihana Gray

## Week 02

1. Writing a program called bank.py 
2. Requirement: The program should: Prompt the user and read in two money amounts (in cent); Add the two amounts; Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
3. I created a program done in 4 steps:
- Step 1: The values are stored in amount1 and amount2. The program prompts the user to enter 2 money amounts in cents, takes the input as a string and converts it into an integer.
`input()` is used to take user input as a string.
`int()` converts the input into an integer because it needs a numerical value. 
Source: https://www.geeksforgeeks.org/python-input-function/
https://docs.python.org/3/library/functions.html#int

- Step 2: The 2 values are added together. The sum is stored in the total_cents variable.
Source: https://www.w3schools.com/python/python_howto_add_two_numbers.asp

- Step 3: Converting cents to euros and formating the output. 
The total cents are converted to euros by dividing by 100. The result is formatted to two decimal places using an f-string to get the right currency format.
Source: https://stackoverflow.com/questions/33861401/convert-cents-to-euro
https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places
https://www.w3schools.com/python/python_string_formatting.asp

- Step 4: Printing the final result (€2.45)

![alt text](<Screenshot 2025-03-02 131955.png>)

## Week 03

This Python program masks account numbers by replacing all but the last four digits with 'X'. 

It consists of two versions:

First Version: Handles exactly 10-digit account numbers, masking the first six digits and showing only the last four.

Updated Version: Supports account numbers of any length, masking all but the last four digits.

**How It Works**

1. Getting user input: using `input()` function to prompt the account number. It also converts it to a string.
Source: https://pynative.com/python-input-function-get-user-input/
https://stackoverflow.com/questions/45229343/program-in-python-that-will-prompt-the-user-to-enter-an-account-number-consists

2. Validating input length: making sure that the length of input is exactly 10 characters.
Source: https://docs.python.org/3/library/functions.html#len
https://realpython.com/len-python-function/

3. Used string slicing to extract the last 4 characters and used `rjust()` to pad the masked number.
Source: https://www.geeksforgeeks.org/string-slicing-in-python/
https://www.w3schools.com/python/ref_string_rjust.asp
https://www.geeksforgeeks.org/python-string-rjust-method/

**Extra:**

1. Using `len()` to return the numbers in the string. Built in function `>` ensures that the number is larger than 4. 
2. Creating a masked version that replacing all but the last 4 characters.
3. If the account number is 4 or less characters it displays error message. 
Sources: https://www.geeksforgeeks.org/string-rjust-ljust-python/
https://docs.python.org/3/library/stdtypes.html
https://www.geeksforgeeks.org/string-slicing-in-python/#extract-characters-using-negative-indices
https://www.w3schools.com/python/python_operators.asp

![alt text](<Screenshot 2025-03-02 134704.png>)

## Week 04

- A function is defined as `collatz` that takes a single parameter `n`, defined with using `def` keyword.
Source: https://www.w3schools.com/python/python_functions.asp
- The while loop `while n != 1` executes as long as `n != 1` is `True`. It runs until `n` becomes 1.
Source: https://www.w3schools.com/python/python_while_loops.asp
https://realpython.com/python-while-loop/
- The value `n` is printed `print(n, end=" ")` followed by space to keep the output in the same line.
Source: https://www.w3schools.com/python/python_functions.asp
- An `if` statement is used to check if `n` is even or odd: 
  if even: `n % 2 == 0` that means `n` is divided by 2 using integer division `//` ensuring the result is integer.
  else (if odd): `n` is multiplied by 3 and added 1
Source: https://www.w3schools.com/python/python_conditions.asp 
https://realpython.com/python-while-loop/
- The loop exits when `n` is 1, the final value of `n` is printed.

**User Input:**
- User input is a positive integer. The `input()` function reads a line from input and the converts to integer `int()`
Source: https://www.w3schools.com/python/ref_func_input.asp
- If the integer is positive, it refers to `collatz` function. If not, the user is prompted to enter a positive integer.
Source: https://www.w3schools.com/python/python_conditions.asp
- Exception `except` is added to block potential errors with different values. if `ValueError` occurs, the user is prompted
to enter a positive integer.
Source: https://www.geeksforgeeks.org/python-exception-handling/
https://www.w3schools.com/python/python_try_except.asp

![alt text](<Screenshot 2025-03-03 094434.png>)

