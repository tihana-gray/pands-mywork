# Programming and Scripting: My Weekly Tasks

by Tihana Gray

---

## 📅 Week 02

**Task:**

Writing a program called `bank.py`\
Requirement: The program should: Prompt the user and read in two money amounts (in cent); Add the two amounts; Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.

### Steps:
1. **Input Handling:**
- The values are stored in amount1 and amount2. The program prompts the user to enter 2 money amounts in cents, takes the input as a string and converts it into an integer.\
`input()` is used to take user input as a string.\
`int()` converts the input into an integer because it needs a numerical value.\
📚 Source: https://www.geeksforgeeks.org/python-input-function/\
https://docs.python.org/3/library/functions.html#int

2. **Adding the Values:** 
- The 2 values are added together. The sum is stored in the total_cents variable.\
📚 Source: https://www.w3schools.com/python/python_howto_add_two_numbers.asp

3. **Formatting as Euros:** 
- Converting cents to euros and formating the output. 
The total cents are converted to euros by dividing by 100. The result is formatted to two decimal places using an f-string to get the right currency format.\
📚 Source: https://stackoverflow.com/questions/33861401/convert-cents-to-euro\
https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places\
https://www.w3schools.com/python/python_string_formatting.asp\

4. **Final Output:** 
- Printing the final result (€2.45)

![bank.py output](<Screenshot 2025-03-02 131955.png>)

---

## 📅 Week 03

This Python program masks account numbers by replacing all but the last four digits with 'X'.\
It consists of two versions:\
- First Version: Handles exactly 10-digit account numbers, masking the first six digits and showing only the last four.
- Updated Version: Supports account numbers of any length, masking all but the last four digits.

### How it works:

1. **User Input:**
- Using `input()` function to prompt the account number. It also converts it to a string.
📚 Source: https://pynative.com/python-input-function-get-user-input/\
https://stackoverflow.com/questions/45229343/program-in-python-that-will-prompt-the-user-to-enter-an-account-number-consists

2. **Validating input length:**
- Making sure that the length of input is exactly 10 characters.\
📚 Source: https://docs.python.org/3/library/functions.html#len\
https://realpython.com/len-python-function/

3. **Masking:**
- Used string slicing to extract the last 4 characters and used `rjust()` to pad the masked number.\
📚 Source: https://www.geeksforgeeks.org/string-slicing-in-python/\
https://www.w3schools.com/python/ref_string_rjust.asp\
https://www.geeksforgeeks.org/python-string-rjust-method/

### Extra:

1. Using `len()` to return the numbers in the string. Built in function `>` ensures that the number is larger than 4. 
2. Creating a masked version that replacing all but the last 4 characters.
3. If the account number is 4 or less characters it displays error message.\ 
📚 Sources: https://www.geeksforgeeks.org/string-rjust-ljust-python/\
https://docs.python.org/3/library/stdtypes.html\
https://www.geeksforgeeks.org/string-slicing-in-python/#extract-characters-using-negative-indices\
https://www.w3schools.com/python/python_operators.asp

![terminal output](<Screenshot 2025-03-02 134704.png>)

---

## 📅 Week 04

Writing a program, called `collatz.py`, that asks the user to input any positive integer and outputs the successive values of the following calculation.\
At each step calculates the next value by taking the current value and, if it is even, dividing it by two, but if it is odd, multiplying it by three and adding one.\
The program ends if the current value is one.

1. **Colatz:**
- A function is defined as `collatz` that takes a single parameter `n`, defined with using `def` keyword.\
📚 Source: https://www.w3schools.com/python/python_functions.asp

2. **Loop:**
- The while loop `while n != 1` executes as long as `n != 1` is `True`. It runs until `n` becomes 1.\
📚 Source: https://www.w3schools.com/python/python_while_loops.asp\
https://realpython.com/python-while-loop/

3. **Value:**
- The value `n` is printed `print(n, end=" ")` followed by space to keep the output in the same line.\
📚 Source: https://www.w3schools.com/python/python_functions.asp

4. **Conditions:**
- An `if` statement is used to check if `n` is even or odd:\
  if even: `n % 2 == 0` that means `n` is divided by 2 using integer division `//` ensuring the result is integer.\
  else (if odd): `n` is multiplied by 3 and added 1.\
📚 Source: https://www.w3schools.com/python/python_conditions.asp\
https://realpython.com/python-while-loop/
- The loop exits when `n` is 1, the final value of `n` is printed.

### User Input:
- User input is a positive integer. The `input()` function reads a line from input and the converts to integer `int()`\
📚 Source: https://www.w3schools.com/python/ref_func_input.asp
- If the integer is positive, it refers to `collatz` function. If not, the user is prompted to enter a positive integer.\
📚 Source: https://www.w3schools.com/python/python_conditions.asp
- Exception `except` is added to block potential errors with different values. if `ValueError` occurs, the user is prompted
to enter a positive integer.\
📚 Source: https://www.geeksforgeeks.org/python-exception-handling/\
https://www.w3schools.com/python/python_try_except.asp

![collatz output](<Screenshot 2025-03-03 094434.png>)

---

## 📅 Week 05

Writing a program that outputs whether or not today is a weekday.

1. **Datetime:**
- First the `datetime` modul is imported. It is needed to show the current day.\
📚 Source: https://docs.python.org/3/library/datetime.html

2. **Tuple:**
- Next, `weekdays` tuple is set to contain names of working days and 'weekends` tuple is for weekend days.\
📚 Source: https://www.w3schools.com/python/python_tuples.asp\ 
https://www.w3schools.com/python/gloss_python_tuple.asp\ 
https://www.datacamp.com/tutorial/python-tuples-tutorial

3. **Dictionary:**
- Dictionary mapping helps adding numbers to day names. Integers are created for each weekdays, further creating a loop using numbers as keys.\
📚 Source: https://realpython.com/python-dicts/\ 
https://stackoverflow.com/questions/36341484/get-day-name-from-weekday-int

4. **Weekday function:**
- The `datetime.now().weekday()` function is used to return the integer value corresponding to the specified day of the week.\
📚 Source: https://www.geeksforgeeks.org/weekday-function-of-datetime-date-class-in-python/

5. **Conversion:**
- Next step retrieves the day name from `day_map` using the integer from `weekday()` to convert numbers into words.\
📚 Source: https://realpython.com/python-dicts/\ 
https://www.w3schools.com/python/python_dictionaries.asp\ 
https://www.w3schools.com/python/python_ref_dictionary.asp

6. **Output:**
- By using a set item `if today_name in set(weekdays)`the day of the week is checked. Used approach is Python Set, Python Loop and checking if item in a set exists.\
Source: https://www.w3schools.com/python/gloss_python_check_if_set_item_exists.asp\ 
https://www.w3schools.com/python/python_sets.asp\ 
https://www.w3schools.com/python/python_sets_join.asp

![weekday checker output](<Screenshot 2025-03-18 211432.png>)