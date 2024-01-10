import numpy as np
import matplotlib.pyplot as plt

for i in range(0,361):
    x = np.sin(np.radians(i))
    y = np.cos(np.radians(i))
    z = np.tan(np.radians(i))
    print(i, x, y, z,"\n")
