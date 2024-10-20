import numpy as np

R_AB = np.matrix([[0.866, -0.5, 0],
        [0.5, 0.866, 0],
        [0, 0, 1]])

P_B = np.matrix([[0],
       [2], 
       [0]])

print(R_AB * P_B)