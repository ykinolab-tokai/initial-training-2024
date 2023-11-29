import numpy as np
import matplotlib.pyplot as plt

alpha = -2
beta = 2

a = 1 
b = -6
c = 9
d = -3

x = np.linspace(-5, 5, 100)
y1 = a * x**3 + b * x**2 + c * x + d
y2 = a * (x - alpha) **3 + b * (x - alpha) **2 + c * (x - alpha) + (d + beta)

plt.plot(x, y1)
plt.plot(x, y2)
plt.savefig("q06.png")
