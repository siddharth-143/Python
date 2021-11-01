# Simple Plot

import matplotlib.pyplot as plt

plt.plot([0, 0], [-1, 1], linewidth=5, zorder=3)
plt.plot([-1, 1], [-1, 1], linewidth=5, zorder=2)
plt.plot([-1, 1], [1, -1], linewidth=5, zorder=1)

plt.xlabel("x label", color="r", size=20, labelpad=10)
plt.ylabel("y label")
plt.title("Graph Plot")

plt.show()