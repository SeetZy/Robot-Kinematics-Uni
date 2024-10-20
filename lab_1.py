import numpy as np
import math

# Displacement coordinates (cm) - X, Y, Z axis
x = 29 * 24
y = 29 * 2
z = -143

# Transformation matrix
T = np.matrix([[0, 0, 0, x],
               [0, 0, 0, y],
               [0, 0, 0, z],
               [0, 0, 0, 1]])

print(T)