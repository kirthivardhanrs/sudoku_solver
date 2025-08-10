import numpy as np
import csv

sudoku = []

with open('input.csv') as f:
    data = csv.reader(f, delimiter=',')
    for row in data:
        row = [int(x) for x in row]
        sudoku.append(row)

sudoku = np.array(sudoku)
sudoku = sudoku.reshape(3,3,3,3).transpose(0, 2, 1, 3) # allows for more intuitive data access

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
    flat_coord = np.ravel_multi_index((a,b,c,d), sudoku.shape) + 1
    while flat_coord < sudoku.size:
        if sudoku.flatten()[flat_coord] == 0:
            return np.unravel_index(flat_coord, sudoku.shape)
        flat_coord += 1
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
                next_empty = get_next_empty(sudoku, a, b, c, d)
                if next_empty != False:
                    return solve(sudoku, next_empty)
                else:
                    with open('input.csv', 'w') as f:
                        wr = csv.writer(f)
                        wr.writerows(sudoku.transpose(0,2,1,3).reshape(9,9))
                    return
        sudoku[a,b,c,d] = 0
        return solve(sudoku, prev[-1])


solve(sudoku, [0,0,0,0])



#sudoku[a,b,c,d] = ath row of big 3x3, bth col of big 3x3, cth row of selected small 3x3, infer for d