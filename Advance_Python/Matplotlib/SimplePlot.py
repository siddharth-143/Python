# Simple Plot

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 2, 3], linewidth=5, zorder=3)

plt.xlabel("x label", color="r", size=20, labelpad=10)
plt.ylabel("y label")
plt.title("Graph Plot")

plt.show()