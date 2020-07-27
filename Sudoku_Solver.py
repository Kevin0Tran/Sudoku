import numpy as np
s =  np.array([[0,7,9,1,3,2,0,8,5],
                [0,6,0,5,9,0,7,0,0],
                [5,0,8,7,0,0,2,1,0],
                [0,0,0,8,0,0,9,0,0],
                [7,0,6,3,4,0,0,0,0],
                [8,0,1,2,0,0,4,0,3],
                [0,8,7,0,0,0,3,0,0],
                [9,0,3,0,0,0,5,0,8],
                [2,5,0,0,0,0,1,9,0]])

def solver(number,row, column, matrix):
        for a in range(0,9): #checks by  row
            if number == matrix[row][a]:
                return False
        for b in range(0,9):  #checks by column
            if number == matrix[b][column]:
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
                for number in range (1,9):
                        if (solver(number,row,column,matrix)) == True:
                            matrix[column][row] = number
                        else: matrix[column][row] = 0 #not sure f I need, will double check tomorrow
    #sudoku(matrix)
    print(matrix)

sudoku(s)
