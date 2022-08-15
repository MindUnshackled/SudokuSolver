import numpy as np

# puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#         [6, 0, 0, 1, 9, 5, 0, 0, 0],
#         [0, 9, 8, 0, 0, 0, 0, 6, 0],
#         [8, 0, 0, 0, 6, 0, 0, 0, 3],
#         [4, 0, 0, 8, 0, 3, 0, 0, 1],
#         [7, 0, 0, 0, 2, 0, 0, 0, 6],
#         [0, 6, 0, 0, 0, 0, 2, 8, 0],
#         [0, 0, 0, 0, 1, 9, 0, 0, 5],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
puzzle1 = [[0, 0, 8, 2, 4, 7, 9, 0, 3],
          [0, 3, 0, 1, 0, 0, 0, 8, 0],
          [9, 1, 7, 0, 0, 3, 0, 5, 0],
          [0, 6, 0, 3, 0, 0, 0, 0, 0],
          [0, 7, 0, 0, 5, 8, 0, 6, 0],
          [1, 0, 9, 6, 7, 0, 0, 0, 0],
          [2, 9, 6, 0, 0, 1, 3, 0, 0],
          [0, 0, 0, 4, 3, 9, 0, 0, 6],
          [0, 0, 3, 5, 2, 6, 0, 0, 1]]

puzzle2 = [[0, 0, 3, 0, 0, 0, 0, 0, 2],
           [0, 0, 5, 6, 1, 0, 8, 0, 0],
           [9, 8, 7, 0, 0, 0, 6, 0, 0],
           [0, 0, 1, 2, 0, 0, 0, 0, 5],
           [0, 0, 0, 0, 6, 0, 0, 0, 0],
           [5, 0, 0, 0, 0, 3, 4, 0, 0],
           [0, 0, 2, 0, 0, 0, 5, 9, 8],
           [0, 0, 8, 0, 7, 5, 3, 0, 0],
           [6, 0, 0, 0, 0, 0, 1, 0, 0]]
puzzle3 = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 3, 6, 0, 0, 0, 0, 0],
           [0, 7, 0, 0, 9, 0, 2, 0, 0],
           [0, 5, 0, 0, 0, 7, 0, 0, 0],
           [0, 0, 0, 0, 4, 5, 7, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 3, 0],
           [0, 0, 1, 0, 0, 0, 0, 6, 8],
           [0, 0, 8, 5, 0, 0, 0, 1, 0],
           [0, 9, 0, 0, 0, 0, 4, 0, 0]]
print("Original: ", "\n", np.matrix(puzzle3), "\n")

# def findEmpty(puzzle):
#     for row in range(9):
#         for col in range(9):
#             if puzzle[row][col] == ".":
#                 return row, col
#     return -1, -1

def check(row, col, num):
    global puzzle3
    for i in range(9):
        if puzzle3[row][i] == num:
            return False

    for i in range(9):
        if puzzle3[i][col] == num:
            return False

    r = (row // 3) * 3
    c = (col // 3) * 3
    for a in range(3):
        for b in range(3):
            if puzzle3[r + a][c + b] == num:
                return False

    return True

# def checkRow(row, num, puzzle):
#     for col in range(9):
#         if puzzle[row][col] == num:
#             return False
#     return True
#
# def checkCol(col, num, puzzle):
#     for row in range(9):
#         if puzzle[row][col] == num:
#             return False
#     return True
#
# def checkSquare(row, col, num, puzzle):
#     for r in range(row, row + 3):
#         for c in range(col, col + 3):
#             if puzzle[row][col] == num:
#                 return False
#     return True

def solve():
    global puzzle3
    for row in range(9):
        for col in range(9):
            if puzzle3[row][col] == 0:
                for num in range(1, 10):
                    if check(row, col, num):
                        puzzle3[row][col] = num
                        solve()
                        puzzle3[row][col] = 0
                return
    print("Solved: ", "\n", np.matrix(puzzle3))

solve()
# print("Solved: ", "\n", np.matrix(puzzle))


