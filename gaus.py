#!/usr/bin/env python

A = [[1,2,13],
    [3,4,29]]


rows = len(A)
cols = len(A[0])



#def solve(A, n)

for k in range(0,rows - 1): #Current row used (k)
    print("A=",A)
    for i in range(k+1, rows): #Selectes the next row... the one to change
        pivot_mult = A[i][k]/ A[k][k]
        for j in range(0, cols): #The specific column number in that row
            A[i][j] = A[i][j] - (pivot_mult) * A[k][j]


print("Solution is: ", A)
