import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.01,5,0.001)
y = np.log(x)
y1 = np.log2(x)
y2 = np.log10(x)

plt.xlim(0.01,5)
plt.plot(x,y,label="y = log x")
plt.plot(x,y1,label="y = log2 x")
plt.plot(x,y2,label="y = log10 x")
plt.legend()
plt.show()
plt.savefig("q08")