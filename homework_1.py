import numpy as np

# System B
Bx = 14
By = 1
Bz = 9.5

# System S
Sx = 5.5
Sy = 4
Sz = -2.5

# System G
Gx = 5
Gy = 9.5

BT_T = np.matrix([[0, 0.87, 0.5],
                  [0, -0.5, 0.87],
                  [1, 0, 0]])

BS_T = np.matrix([[0, -1, 0],
                  [1, 0, 0],
                  [0, 0, 1]])

SG_T = np.matrix([[],
                  [],
                  []])

TS_T = BT_T * BS_T

print(TS_T)