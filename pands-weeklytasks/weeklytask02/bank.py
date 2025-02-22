# Weekly Tasks 02
# Program that prints and reads the money amounts
# Author: Tihana Gray

# Step 1
amount1 = int(input("Enter amount1 (in cent): "))
amount2 = int(input("Enter amount2 (in cent): "))

# Step 2
total_cents = amount1 + amount2

# Step 3
total_euros = total_cents / 100 
formatted_total = f"€{total_euros:.2f}"

# Step 4
print(f"The total amount is {formatted_total}.")
