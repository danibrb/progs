import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt 
import pandas as pd


df = pd.read_csv('data.csv', delimiter = " ", header=None)
df = pd.DataFrame(df)

x= df[0]
y= df[1]
 
f = interp1d(x, y, kind='cubic')
 
x_new = x
y_new = f(x_new)
 
plt.plot(x_new, y_new, label='Smooth Curve')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Smooth Curve with Interpolation Example')
plt.legend()
plt.show()