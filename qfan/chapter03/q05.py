import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 5)
print(x)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
for i in range(5):
    print(i,y1[i],y2[i],y3[i],"\n")
