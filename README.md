# Backtracking Sudoku Solver

Uses brute force backtracking to solve 9x9 sudokus, inputted from [input.csv](input.csv). I've since learnt that Python may not be the best to implement this particular algorithm since it does not optimize for tail recursion, so I've had to artifically increase the recursion limit using `sys.setrecursionlimit(4000)`, which isn't the best idea.   

Hopefully I find a better Python algorithm or use a different language for tail calls.