# Histogram of normal distribution + plot of h(x) = x^3 on same axes
# Author: Tihana Gray


import numpy as np
import matplotlib.pyplot as plt

# Generating 1000 values from a normal distribution
mean = 5
std_dev = 2
num_values = 1000
normal_data = np.random.normal(loc=mean, scale=std_dev, size=num_values)

# Creating x values and compute h(x) = x^3
x = np.linspace(0, 10, 400)
h_x = x**3

# Creating the plot
plt.figure(figsize=(10, 6))  # Makes it a bit wider and nicer

# Plotting histogram
plt.hist(normal_data, bins=30, alpha=0.6, label="Normal distribution", color='skyblue', edgecolor='black')

# Plotting h(x) = x^3
plt.plot(x, h_x, label="h(x) = x³", color='darkred', linewidth=2)

# Making it pretty
plt.title("Histogram and h(x) = x³ on the same plot")
plt.xlabel("x / Value")
plt.ylabel("Frequency / h(x)")
plt.legend()
plt.grid(True)

# Saving the figure
plt.savefig("plottask.png", dpi=300)

# Showing the plot
plt.show()
