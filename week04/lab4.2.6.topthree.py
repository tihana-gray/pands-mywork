# This program generates 10 random numbers
# prints them out, then prints out the top 3

# Author: Tihana Gray

# I will use a list to store and manipulate the numbers

import random
# Programming the general case
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range(0, howMany):
    numbers.append(random.randint(rangeFrom, rangeTo))
print (f"{howMany} random numbers\t {numbers}")

# I am keeping the original list so I can print it out again
topOnes = numbers.copy()

topOnes.sort(reverse = True)
print ("The top", topHowMany, "are\t\t", topOnes[0:topHowMany])