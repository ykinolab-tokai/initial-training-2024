import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,100)
y1=x**3 - 6*x**2+9*x-3
y2=(x+2)**3-6*(x+2)**2+9*(x+2)-1
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()