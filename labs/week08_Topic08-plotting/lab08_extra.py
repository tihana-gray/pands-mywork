# testing the plotting functions
# messing with seaborn
# Author: Tihana Gray

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate 100 random salaries with a normal distribution
salaries = np.random.normal(loc=50000, scale=10000, size=100)

# Plot a histogram + KDE line (smooth curve like a normal distribution)
# https://seaborn.pydata.org/generated/seaborn.kdeplot.html

sns.histplot(salaries, kde=True, bins=20, color='skyblue')

plt.title("Salaries Distribution with Normal Curve")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()
