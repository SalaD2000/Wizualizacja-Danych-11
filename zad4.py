import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure( figsize =( 10 , 20 ))

ax1 = fig.add_subplot( 331 , projection = '3d' )
ax2 = fig.add_subplot( 332 , projection = '3d' )
ax3 = fig.add_subplot( 333 , projection = '3d' )
ax4 = fig.add_subplot( 334 , projection = '3d' )
ax5 = fig.add_subplot( 335 , projection = '3d' )
ax6 = fig.add_subplot( 336 , projection = '3d' )

_x = np.arange( 4 )
_y = np.arange( 5 )
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax1.bar3d(x, y, bottom, width, depth, top, shade = True , color='Red')
ax1.set_title('Czerwony cień')

ax2.bar3d(x, y, bottom, width, depth, top, shade = False , color='Red')
ax2.set_title('Czerwony')

ax3.bar3d(x, y, bottom, width, depth, top, shade = False , color='Green')
ax3.set_title('Zielony cień')

ax4.bar3d(x, y, bottom, width, depth, top, shade = True , color='Green')
ax4.set_title('Zielony')

ax5.bar3d(x, y, bottom, width, depth, top, shade = True , color='Blue')
ax5.set_title('Niebieski cień')

ax6.bar3d(x, y, bottom, width, depth, top, shade = True , color='Blue')
ax6.set_title('Niebieksi')

plt.show()