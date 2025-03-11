# Creating a program that puts 10 random numbers into a queue(list)
# the program should then output all the values in the queue
# then take the numbers from the queue one at a time, print it and the current numbers still in the queue
# the (the command pop(0) takes the first element out of a list)

# Author: Tihana Gray

import random
queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range(numberOfNumbers): 
    queue.append(random.randint(0, rangeTo))

print(f"Queue is: {queue}")

# Removing elements from the queue one at a time
while len(queue) != 0:
    currentNumber = queue.pop(0)
    print(f"Current number is {currentNumber} and the queue is {queue}") # added f string

print("The queue is now empty") 
