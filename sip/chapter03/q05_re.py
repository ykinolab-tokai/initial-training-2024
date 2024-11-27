import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0,361)
rad = theta * np.pi/180
sin = [np.sin(i) for i in rad]
cos = [np.cos(i) for i in rad]
tan = [np.tan(i) for i in rad]

print(f"θ°  sinθ   cosθ   tanθ")
print("---------------------------")
for i,(s,c,t) in enumerate(zip(sin,cos,tan)):
  print(f"{i} | {s:.5f}  {c:.5f}  {t:.5f}\n")