import numpy as np
import matplotlib.pyplot as plt

for i in range(1, 361):
    rad = i * np.pi / 180
    sin = np.sin(rad)
    cos = np.cos(rad)
    tan = np.tan(rad)

    print(f"θ[°]: {i} sinθ: {sin:.5f} cosθ: {cos:.5f} tanθ: {tan:.5f}")
