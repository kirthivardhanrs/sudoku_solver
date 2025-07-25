import numpy as np
import csv
import sys

sys.setrecursionlimit(4000)

sudoku = np.array(
    [[[[5, 3, 0], [6, 0, 0], [0, 9, 8]],
    [[0, 7, 0], [1, 9, 5], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 6, 0]]],
    [[[8, 0, 0], [4, 0, 0], [7, 0, 0]],
    [[0, 6, 0], [8, 0, 3], [0, 2, 0]],
    [[0, 0, 3], [0, 0, 1], [0, 0, 6]]],
    [[[0, 6, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [4, 1, 9], [0, 8, 0]],
    [[2, 8, 0], [0, 0, 5], [0, 7, 9]]]]
)

def valid_set(arr, num):
    if num in arr:
        return False
    return True

def checks(puzzle, a, b, c, d, num):
    col_check = valid_set(puzzle[:, b, :, d].flatten(), num)
    row_check = valid_set(puzzle[a, :, c, :].flatten(), num)
    grid3x3_check = valid_set(puzzle[a, b, :, :].flatten(), num)

    return col_check and row_check and grid3x3_check


def get_next_empty(sudoku, a, b, c, d):
    check_flag = False
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for m in range(3):
                    if [i,j,k,m] == [a,b,c,d]:
                        check_flag = True
                        continue
                    if not sudoku[i, j, k, m] and check_flag == True:
                        return [i, j, k, m]
    return False

prev = []

def solve(sudoku, abcd):
    a, b, c, d = abcd
    n = 0
    try:
        if abcd == prev[-1]:
            prev.pop()
            n = sudoku[a,b,c,d]
    except IndexError: # the if statement produces this error when prev is initialized
        pass
    if sudoku[a,b,c,d] and n == 0:
        return solve(sudoku, get_next_empty(sudoku, a, b, c, d))
    else:
        for i in range(n, 9):
            if checks(sudoku, a, b, c, d, i+1):
                sudoku[a,b,c,d] = i+1
                prev.append([a,b,c,d])
                if get_next_empty(sudoku, a, b, c, d) != False:
                    return solve(sudoku, get_next_empty(sudoku, a, b, c, d))
                else:
                    with open('sudoku.csv', 'w') as f:
                        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
                        wr.writerow(sudoku.flatten())
                    return
        sudoku[a,b,c,d] = 0
        return solve(sudoku, prev[-1])
        

solve(sudoku, [0,0,0,0])



#sudoku[a,b,c,d] = ath row of big 3x3, bth col of big 3x3, cth row of selected small 3x3, infer for d