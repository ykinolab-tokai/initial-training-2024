import numpy as np

a = ['θ[$^\circ$]', 'sinθ', 'cosθ', 'tanθ']
b = np.full((361, 4), .0)

for i in range(361):
    x = ((2 * np.pi) / 360) * i
    b[i, 0] = i
    b[i, 1] = np.sin(x)
    b[i, 2] = np.cos(x)
    b[i, 3] = np.tan(x)

print(a)
print(b)
