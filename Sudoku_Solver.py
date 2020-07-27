import numpy as np
s =  np.array([[5,0,0,0,8,0,0,4,9],
                [0,0,0,5,0,0,0,3,0],
                [0,6,7,3,0,0,0,0,1],
                [1,5,0,0,0,0,0,0,0],
                [0,0,0,2,0,8,0,0,0],
                [0,0,0,0,0,0,0,1,8],
                [7,0,0,0,0,4,1,5,0],
                [0,3,0,0,0,2,0,0,0],
                [4,9,0,0,5,0,0,0,3]])

def solver(number,row, column, matrix):
        for a in range(0,9): #checks by  row
            if number == matrix[column][a]:
                return False
        for b in range(0,9):  #checks by column
            if number == matrix[b][row]:
                return False
        x0 = (row//3)*3
        y0 = (column//3)*3
        for i in range(0,3): #checks by 3x3 grid
            for j in range(0,3):
                if number == matrix[x0+i][y0+j]:
                    return False
        return True

def sudoku(matrix):
    #checks each column and row for  0-9 to see if it fits in spots with 0
    for column in range(0,9):
        for row in range(0,9):
            if matrix[column][row] == 0:
                for number in range (1,10):
                    if solver(number,row,column,matrix):
                        matrix[column][row] = number
                sudoku(matrix)
            #return
    print(matrix)

sudoku(s)
