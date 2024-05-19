board = []
print("Enter the Sudoku puzzle row by row (use 0 for empty spaces):")
for i in range(9):
    while True:
        try:
            row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
            if len(row) != 9:
                raise ValueError("Each row must have exactly 9 numbers.")
            board.append(row)
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter the row again.")

print("Initial Sudoku board:")
for row in board:
    print(" ".join(str(num) if num != 0 else '.' for num in row))

empty_locations = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def is_valid(board, num, pos):
    for x in range(9):
        if board[pos[0]][x] == num or board[x][pos[1]] == num:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for x in range(box_y * 3, box_y * 3 + 3):
        for y in range(box_x * 3, box_x * 3 + 3):
            if board[x][y] == num:
                return False
    return True

def solve(board):
    if not empty_locations:
        return True
    row, col = empty_locations.pop(0)
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    empty_locations.insert(0, (row, col))
    return False

if solve(board):
    print("Sudoku puzzle solved successfully!")
else:
    print("No solution exists for the given Sudoku puzzle.")

print("Solved Sudoku board:")
for row in board:
    print(" ".join(str(num) for num in row))
