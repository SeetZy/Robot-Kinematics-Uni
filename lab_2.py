import numpy as np

I = np.matrix([[118.4, 135.2]])

C = np.matrix([[3, 3.5],
               [3.2, 3.6]])

# Inverse matrix C to get the divide the matrixes
P = I * np.linalg.inv(C)

print(P)