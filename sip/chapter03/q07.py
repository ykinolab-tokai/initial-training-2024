import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2,2,0.001)
y = 2**x

y1 = 2**(-x)

plt.xlim(-2,2)
plt.plot(x,y,label="y = 2^x")
plt.plot(x,y1,label="y = 2^-x")
plt.legend()
plt.show()