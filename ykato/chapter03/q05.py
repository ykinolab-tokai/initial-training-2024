import numpy as np

a = ['θ,sinθ,cosθ,tanθ']
b = np.arange(0, 361, 1)
c = np.full((361, 3), 0.)

print(a)

for i in range(361):
    x = ((2 * np.pi) / 361) * i

    c[i, 0] = np.sin(x)
    c[i, 1] = np.cos(x)
    c[i, 2] = np.tan(x)

    print('{:5d}'.format(b[i]), end="")
    print(c[i:i+1,::])
