# messing with matplotlib
# Author: Tihana Gray

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label= "xsquared")
plt.plot(xpoints, xpoints, label="straight", color="blue")
plt.legend()
plt.savefig("messingWithPlots.png")

randompoints = np.random.randint(1, 1000, 100)
plt.scatter(xpoints, randompoints, label="random")

plt.show()
