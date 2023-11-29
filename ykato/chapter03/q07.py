import numpy as np
import matplotlib.pyplot as plt

a = 2
b = 2

x = np.linspace(-2, 2, 100)
y1 = a**x
y2 = b**(-x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.savefig("q07.png")
