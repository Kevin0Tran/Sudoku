import numpy as np
s =  np.array([[1,12,131,14,5,6,7,8,9],
    [1,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0],
    [3,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0],
    [5,0,0,0,0,0,0,0,0],
    [6,0,0,0,0,0,0,0,0]])

def possible(number,row, column, matrix):
        for a in range(0,9):
            if number == matrix[row][a]:
                return False
            for b in range(0,9):   #checks the column
                if number == matrix[b][column]:
                    return False
        x0 = (x//3)*3 #how to check the  3X3 matrix slice
        y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):



print(possible(4,s))