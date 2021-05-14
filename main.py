
import numpy as np

board =    [[8, 1, 0, 0, 3, 0, 0, 2, 7],
            [0, 6, 2, 0, 5, 0, 0, 9, 0],
            [0, 7, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 6, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 2, 0, 0, 0, 4],
            [0, 0, 8, 0, 0, 5, 0, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 2, 0, 0, 1, 0, 7, 5, 0],
            [3, 8, 0, 0, 7, 0, 0, 4, 2]]



# print(np.matrix(board))                       #uses numpy function to print out the desired output of the board

def potential_number (r, c, n):                 #parameters are: 'row', 'column', 'number'.
    global board                                #uses the board outside the function

    # is the number appearing in the row?
    for i in range(0, 9):
        if board[r][i] == n:
            return False
    # is the number appearing in the column?
    for i in range(0, 9):
        if board[i][c] == n:
            return False
    # is the number appearing in the square?
    r0 = (r//3) * 3                             #starting point inside the square (0, 3, 6)
    c0 = (c//3) * 3                             #regardless on which row or column you pass in

    for i in range(0, 3):                       #iterate over the three rows inside the square
        for j in range(0, 3):                   #iterate over the three columns inside the square
            if board[r0+i][c0+j] == n:
                return False
    return True                                 #possible number for the given row, column


def solve_board ():
    global board

    for r in range(0, 9):                       #iterate each row in range of 0 - 9
        for c in range(0, 9):                   #iterate each column in range of 0 - 9
            if board[r][c] == 0:                #if a space is 0/empty, it will iterate through numbers -
                for n in range(1, 10):          #in range 1-9
                    if potential_number(r, c, n):   #calling the function for potential number it will fill the number.
                        board[r][c] = n
                        solve_board()
                        board[r][c] = 0
                return

    print(print(np.matrix(board)))


solve_board()








