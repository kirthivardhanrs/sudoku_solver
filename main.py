import numpy as np
import csv

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

sudoku = np.array(
    [[[[5, 3, 4], [6, 7, 2], [1, 9, 8]],
    [[6, 7, 8], [1, 9, 5], [3, 4, 2]],
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

sudoku_test = np.array(
    [[[[5, 3, 4], [6, 7, 2], [1, 9, 8]],
    [[6, 7, 8], [1, 9, 5], [2, 3, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 6, 0]]],
    [[[8, 0, 0], [4, 0, 0], [7, 0, 0]],
    [[0, 6, 0], [8, 0, 3], [0, 2, 0]],
    [[0, 0, 3], [0, 0, 1], [0, 0, 6]]],
    [[[0, 6, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [4, 1, 9], [0, 8, 0]],
    [[2, 8, 0], [0, 0, 5], [0, 7, 9]]]]
)

# print(checks(sudoku_test,0,1,2,1,4))

coords = [] #


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

# print(get_next_empty(sudoku, 0, 0, 2, 0))

prev = []

def solve(sudoku, abcd):
    a, b, c, d = abcd
    n = 0
    try:
        if abcd == prev[-1]:
            prev.pop()
            n = sudoku[a,b,c,d]
    except IndexError:
        pass
    if sudoku[a,b,c,d] and n == 0:
        if not get_next_empty(sudoku, a, b, c, d):
            print("Woah")
            return
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