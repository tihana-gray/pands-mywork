# Programming and Scripting: My Weekly Tasks

by Tihana Gray

## Week 02

1. Writing a program called bank.py 
2. Requirement: The program should: Prompt the user and read in two money amounts (in cent); Add the two amounts; Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
3. I created a program done in 4 steps:
- Step 1: The values are stored in amount1 and amount2. The program prompts the user to enter 2 money amounts in cents, takes the input as a string and converts it into an integer. 
- Step 2: The 2 values are added together. The sum is stored in the total_cents variable.
- Step 3: Converting cents to euros and formating the output. 
- Step 4: Printing the final result (€2.45)

## Week 03

This Python program masks account numbers by replacing all but the last four digits with 'X'. 

It consists of two versions:

First Version: Handles exactly 10-digit account numbers, masking the first six digits and showing only the last four.

Updated Version: Supports account numbers of any length, masking all but the last four digits.

How It Works

The program prompts the user to input an account number.

Depending on the version:
If the input is exactly 10 digits, it replaces the first 6 digits with 'X'.
If the input is of any length greater than 4, it replaces all but the last four digits with 'X'.
The modified account number is then displayed.
