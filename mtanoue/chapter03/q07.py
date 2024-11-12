import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-2,2,0.1)
print(x)
y1=2**x
y2=2**(-x)
plt.plot(x,y1)
plt.plot(x,y2)
plt.savefig("/home/machitanoue/initial-training-2024/mtanoue/chapter03/q07.jpg")

