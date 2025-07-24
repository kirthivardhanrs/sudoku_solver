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

def valid_set(arr, num):
    if num in arr:
        return False
    return True

def checks(puzzle, a, b, c, d, num):
    col_check = valid_set(puzzle[:, b, :, d].flatten(), num)
    row_check = valid_set(puzzle[a, :, c, :].flatten(), num)
    grid3x3_check = valid_set(puzzle[a, b, :, :].flatten(), num)

    return col_check and row_check and grid3x3_check

coords = [] # append([a,b,c,d])
    
# for a in range(3):
#     for b in range(3):
#         for c in range(3):
#             for d in range(3):
#                 if not sudoku[a,b,c,d]:
#                     pass

def get_next_empty(sudoku, a, b, c, d):
    for i in range(a, 3):
        for j in range(b, 3):
            for k in range(c, 3):
                for m in range(d, 3):
                    if not sudoku[i, j, k, m]:
                        return [i, j, k, m]
    return False

print(get_next_empty(sudoku, 0, 2, 2, 2)) # TODO

prev = []

def solve(sudoku, abcd):
    a, b, c, d = abcd
    if sudoku[a,b,c,d]:
        if not get_next_empty(sudoku, a, b, c, d):
            print("Woah")
            return
        return solve(sudoku, get_next_empty(sudoku, a, b, c, d))
    else:
        for i in range(9):
            if checks(sudoku, a, b, c, d, i+1):
                sudoku[a,b,c,d] = i+1
                prev.append([a,b,c,d])
                return solve(sudoku, get_next_empty(sudoku, a, b, c, d))
        sudoku[a,b,c,d] = 0
        return solve(sudoku, prev.pop())
        

solve(sudoku, [0,0,0,0])



#sudoku[a,b,c,d] = ath row of big 3x3, bth col of big 3x3, cth row of selected small 3x3, infer for d