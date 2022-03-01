#!/usr/bin/env python
A1 = [1, 2, 13]
A2 = [3, 4, 29]
A = [A1, A2]
print(A)
n = len(A)



#def solve(A, n):
row_used = 0
row_work_on= 0
for row_used in range(0,n):

    print("First Test")

    for row_work_on in range(row_used +1, n):

        print("Second Test")

        elimination_column = row_work_on -1

        print(A[row_work_on][elimination_column])

        elimination_factor = -1 * A[row_work_on][elimination_column] / A[row_used][row_used]
        print(elimination_factor)

        row_worked_on_column = elimination_column
        print(row_worked_on_column)

        for row_worked_on_column in range(row_work_on-1, n+1):
            print("Third test")
            A[row_work_on][row_worked_on_column] = elimination_factor * A[row_used][row_worked_on_column] + A[row_work_on][row_worked_on_column]
    




                #return(A)
print(A)
