import numpy as np

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

def check_valid(arr):
    return len(arr) == len(set(arr)) and len(arr) == 9

def col_check(puzzle, b, d):
    print(puzzle[:, b, :, d].flatten())
    
col_check(sudoku, 0, 0)

#sudoku[a,b,c,d] = ath row of big 3x3, bth col of big 3x3, cth row of selected small 3x3, infer for d