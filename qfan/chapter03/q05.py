import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 4 * np.pi, 360)
print(x)
row=[x for x in range(361)]
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
print("\t sin\t cos\ttan\t")
for i in range(360):
    print(f"{i}\t{round(y1[i],5)}\t{round(y2[i],5)}\t{round(y3[i],5)}\t")
    print()
