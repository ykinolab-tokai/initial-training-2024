import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 4 * np.pi, 360)
<<<<<<< HEAD
print(x)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
print("\t sin\t cos\ttan\t")
for i in range(360):
    print(f"{i}\t{round(y1[i],5)}\t{round(y2[i],5)}\t{round(y3[i],5)}\t")
=======
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
print(" \tsin\tcos\ttan\t")
for i in range(360):
    print(f"{i}\t{format(y1[i],'.5f')} \t{format(y2[i],'.5f')} \t{format(y3[i],'.5f')}")
>>>>>>> 9f5f2dffcc217eee17b62e88f153e0f1a6e5f887
    print()
