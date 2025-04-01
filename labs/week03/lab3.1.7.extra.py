# Detecting an error

# Author: Tihana Gray

message = 'I have eaten ' + str(99) + ' burritos.'
print(message)

# -----------------------------------------------------

# Testing three functions

# Demonstrating int(), float(), and str() functions

# Converting a float to an integer
num_float = 3.9
num_int = int(num_float)  # Will truncate to 3
print("Integer version of 3.9:", num_int)

# Converting an integer to a float
num_int2 = 5
num_float2 = float(num_int2)  # Converts to 5.0
print("Float version of 5:", num_float2)

# Converting an integer to a string
num_int3 = 100
num_str = str(num_int3)  # Converts to "100"
print("String version of 100:", num_str)

# Using conversions in a real scenario
age = input("Enter your age: ")  # Input is always a string
age_next_year = int(age) + 1  # Convert to integer and add 1
print("Next year, you will be", age_next_year)



