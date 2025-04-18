import time


def parse_puzzles(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def sudoku_solver(puzzle):
    board = [[0 if puzzle[i * 9 + j] == '.' else int(puzzle[i * 9 + j]) for j in range(9)] for i in range(9)]
    if solve(board):
        return ''.join(str(num) for row in board for num in row)
    return None

def main():
    puzzles = parse_puzzles('sudoku_input.txt')
    for puzzle in puzzles:
        start = time.time()
        solved = sudoku_solver(puzzle)
        end = time.time()
        print(solved)
        print("Solved in:", end - start, "seconds")

main()
