#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,4,50)

y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x,y1)
plt.plot(x,y2,color='red',linewidth=2.0,linestyle='--')

plt.show()
