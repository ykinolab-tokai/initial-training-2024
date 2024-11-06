import numpy as np
import matplotlib.pyplot as plt

sin = (np.sin(i) for i in range(361))
cos = (np.cos(i) for i in range(361))
tan = (np.tan(i) for i in range(361))


data = [(i,"{:.5f}".format(s),"{:.5f}".format(c),"{:.5f}".format(t)) for i,(s,c,t) in enumerate(zip(sin,cos,tan))]

axis1 = (["theta","sin","cos","tan"])


plt.axis('off')
tabel = plt.table(cellText=data, colLabels=axis1, loc="center")

plt.show()
