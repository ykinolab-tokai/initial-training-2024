import numpy as np
#####第１問#####
a = np.array([1, 2, 3, 4, 5])
print(a)

a.shape
a.dtype
print(a.shape)
print(a.dtype)
print()
#####第2問#####
b = np.array([-6, -3, 0, 3, 6, 9])
print(b)
print()

######第3問##########
a = np.zeros((3, 3))
print(a)
print()

a = np.ones((3, 3))
print(a)
print()

a = np.random.uniform(-1, 1, (3 ,3))
print(a)
print()

a = 2*np.eye(3)
print(a)
print()

#########第4問##########
a = np.random.uniform(-1, 1, (5 ,4))
print(a)
print()
print(a[2, 3])
print()
print(a[[0, 1, 2, 3, 4], [2]])
print()
print((a[[1], [0, 1, 2, 3]]), (a[[3],[0, 1, 2, 3]]))

#########第5問##############
import numpy as np

a = np.arange(0, 361, 1)
b = np.sin(np.deg2rad(a))
c = np.cos(np.deg2rad(a))
d = np.tan(np.deg2rad(a))

print(f"a       sina     cosa    tana")
for a, b, c, d in zip(a, b, c, d):
    print(f"{a}°\t{b:.3f}\t{c:.3f}\t{d:.3f}")

############第6問#################
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y1 = x**3 - 6*(x**2) + 9*x - 3
y2 = (x-2)**3 - 6*((x-2)**2) + 9*(x-2) - 5

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()

##############第7問#################
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 50)
y1 = 2**x
y2 = 2**(-x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()

##############第8問#################
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 2, 50)
y1 = np.log(x)
y2 = np.log2(x)
y3 = np.log10(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()
