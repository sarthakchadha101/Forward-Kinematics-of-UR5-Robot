import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
a, d = [0, -0.425, -0.39225, 0, 0, 0], [0.089159, 0, 0, 0.10915, 0.09465, 0.0823]
alpha = [np.pi / 2, 0, 0, np.pi / 2, -np.pi / 2, 0]
joint_limits = [
    (-360, 360),  #(Base)
    (-180, 180),  #(Shoulder)
    (-180, 180),  #(Elbow)
    (-360, 360),  #(Wrist 1)
    (-360, 360),  #(Wrist 2)
    (-360, 360)   #(Wrist 3)
]