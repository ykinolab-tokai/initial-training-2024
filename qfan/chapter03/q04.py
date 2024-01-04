import numpy as np
a=np.random.randint(1,50,(5,4))
print(a)
print(a[2,3])
print(a[0:6,2:3])
print(a[::2,::2],a[3])

b=[x for x in range(20)]
print(b[::5])