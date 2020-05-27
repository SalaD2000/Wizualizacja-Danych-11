import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
n=5

for c, m, zlow, zhigh in [('r', '>', 0, 30), ('g', '<', 30, 50), ('b', '^', 50, 70), ('y', ',', 70, 80), ('y', '.', 80, 100)]:
    x=randrange(n, zlow, zhigh)
    y=randrange(n, zlow, zhigh)
    z=randrange(n, zlow, zhigh)
    ax.scatter(x, y, z, c=c, marker=m)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()