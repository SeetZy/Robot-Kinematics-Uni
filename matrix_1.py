R_AB = [[0.866, -0.5, 0],
        [0.5, 0.866, 0],
        [0, 0, 1]]

P_B = [[0],
       [2], 
       [0]]

result = [[0],
          [0],
          [0]]

for i in range(len(R_AB)):
    for j in range(len(P_B[0])):
        for k in range(len(P_B)):
            result[i][j] += R_AB[i][k] * P_B[k][j]
            
for r in result:
    print(r)