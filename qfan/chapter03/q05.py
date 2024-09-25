import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 4 * np.pi, 360)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
print(" \tsin\tcos\ttan\t")
for i in range(360):
    print(f"{i}\t{format(y1[i],'.5f')} \t{format(y2[i],'.5f')} \t{format(y3[i],'.5f')}")
    print()
