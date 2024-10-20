import numpy as np

# first way
a = np.matrix('1 2; 3 4')

# second way
b = np.matrix([[1, 2], [3, 4]])

print(a * b)
