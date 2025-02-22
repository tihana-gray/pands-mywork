# This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all the letters to lower case.
# It then outputs the lengths of the original string
# and the normalised one.

# Author: Tihana Gray

rawString = input("Please enter a string: ")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print(f"That String normalised is: {normalisedString}")
print(f"We reduced the input string from {lengthOfRawString} to {lengthOfNormalised} characters.")

