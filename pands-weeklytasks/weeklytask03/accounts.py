# Program that masks an account number and shows only the last 4 digits.

# Author: Tihana Gray

account_number = input("Please enter a 10-digit account number: ")

# Ensuring the input is 10 digits long
if len(account_number) == 10:
    print ("Please enter a 10-digit account number.")

# Masking the account number
masked_account_number = account_number[-4:].rjust(10, '*')
print(masked_account_number)

# ------------------------------------------------------------------------------------------------------------

# Extra: modifying the program to deal with account numbers of any legth.

account_number = input("Please enter an account number: ")
if len(account_number) > 4:
    masked_account = "X" * (len(account_number) - 4) + account_number[-4:]  # Mask everything except the last 4
    print(masked_account)
else:
    print("Error: Account number must have more than 4 digits.")
