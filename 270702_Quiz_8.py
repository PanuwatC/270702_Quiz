import numpy as np
m = int(input("Enter size for square matrix : "))
A = np.ones(m*m).reshape((m, m)) + 1
for i in range (0,m):
    for j in range (0,m):
        if(i < j and j != m):
            A[i,j] =  0
        elif(i == j or j == m):
            A[i,j] =  1
        else:
            A[i,j] =  -1
print("Matrix A size",m,"*",m,": \n",A)
