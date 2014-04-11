from __future__ import division
from numpy import *
from math import *


A = array([(6.0,1.0,1.0),(3.0,2.0,1.0),(1.0,0.0,2.0)])

N = len(A)
L = identity(N)
U = array([(2.0,1.0,1.0),(3.0,2.0,1.0),(1.0,0.0,2.0)])

piv = arange(N)


for k in range(0, N):
    curr_piv = fabs(U[k,k])
    new_piv = k
    for p in range(k+1, N):
        if(curr_piv < fabs(U[piv[p],k])):
            curr_piv = fabs(U[piv[p],k])
            new_piv = p
    
    if(new_piv != k):
        tempPiv = piv[k]
        piv[k] = piv[new_piv]
        piv[new_piv] = tempPiv    
        for i in range(0, k-1):
            tempL = L[k, i]
            L[k, i] = L[new_piv, i]
            L[new_piv, i] = tempL
    
    for i in range(k+1, N):
        L[i,k] = U[piv[i], k]/U[piv[k],k]
        for j in range(0, N):
            U[piv[i], j] = U[piv[i], j] - L[i,k]*U[piv[k],j]

pivot = zeros((N,N))

for b in range(0,N):
    pivot[b, piv[b]] = 1;
disp(pivot)
disp(A)
disp(L)
transU = dot(pivot, U)
disp(transU)

            