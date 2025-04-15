# program that plots the function y = x2
# Author: Tihana Gray

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints #multiply each entry by itself

plt.plot(xpoints, ypoints)
plt.show()
