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

def valid_set(arr):
    return len(arr) == len(set(arr)) and len(arr) == 9

def checks(puzzle, a, b, c, d):
    col_check = valid_set(puzzle[:, b, :, d].flatten())
    row_check = valid_set(puzzle[a, :, c, :].flatten())
    grid3x3_check = valid_set(puzzle[a, b, :, :].flatten())

    return [col_check, row_check, grid3x3_check]

coords = [] # append([a,b,c,d])
    
for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                if not sudoku[a,b,c,d]:
                    pass


#sudoku[a,b,c,d] = ath row of big 3x3, bth col of big 3x3, cth row of selected small 3x3, infer for d