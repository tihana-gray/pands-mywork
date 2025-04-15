# program that makes a list called ages that has, the same number random
# values as salaries
# also includes scatter plot

# Author: Tihana Gray

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high = 65, size = numberOfEntries) 

plt.scatter(ages, salaries ) # this will be random

# add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # multiply each entry by itself

plt.plot(xpoints, ypoints, color='r', label = "x squared")

plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()

#add this line to the end and you can comment out the show()
#plt.show() # see how the axis have changed
plt.savefig('prettier-plot.png')

plt.show() # see how the axis have changed

