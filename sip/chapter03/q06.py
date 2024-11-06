import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5,0.001)
y = x**3 - 6*(x**2) + 9*x - 3

x1 = x-2
y1 = y+2

plt.xlim(-5,5)
plt.plot(x,y,label="y = x**3 - 6*(x**2) + 9*x - 3")
plt.plot(x1,y1,label="x-2,y+2")
plt.legend()
plt.show()