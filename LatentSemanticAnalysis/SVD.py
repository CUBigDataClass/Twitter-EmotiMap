import numpy as np
A = np.array([(6.0,1.0,1.0),(3.0,2.0,1.0),(1.0,0.0,2.0)])
U,S,V = np.linalg.svd(A, full_matrices = True)
print(U)
print(S)
print(V)   