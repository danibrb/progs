from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import pandas as pd

df = pd.read_csv('data.csv')

print(df) 

nodes = np.array( [ [1, 2], [6, 15], [10, 6], [10, 3], [3, 7] ] )

x = nodes[:,0]
y = nodes[:,1]

tck,u     = interpolate.splprep( [x,y] ,s = 0 )
xnew,ynew = interpolate.splev( np.linspace( 0, 1, 100 ), tck,der = 0)

plt.plot( x,y,'o' , xnew ,ynew )
plt.legend( [ 'data' , 'spline'] )
plt.axis( [ x.min() - 1 , x.max() + 1 , y.min() - 1 , y.max() + 2 ] )
plt.show()