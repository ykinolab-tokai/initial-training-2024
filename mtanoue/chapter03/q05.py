import numpy as np
import matplotlib.pyplot as plt

print("θ [°]|tsin(θ)\tcos(θ\ttan(θ))")

for angle in range(361): #0から360°まで
    radians=np.radians(angle) #角度をラジアンに変換
    sin=np.sin(radians)
    cos=np.cos(radians)
    if cos ==0: #cosが0になる時はtanは定理しない
        tan="undefined"
    else:
        tan=np.tan(radians)
    print(f"{angle}\t{sin:.5f}\t{cos:.5f}\t{tan:.5f}")
