import numpy as np

a = np.random.random((5,4))

b = a[2,3]

c = a[0:5,2]

for i in range(len(a)):
    if i % 2 != 0:
        d = a[i,:]
