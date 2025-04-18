from ortools.sat.python import cp_model
import time

def parse_puzzles(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def solve_sudoku(puzzle):
    model = cp_model.CpModel()
    grid = {}
    for i in range(9):
        for j in range(9):
            grid[(i, j)] = model.NewIntVar(1, 9, f'cell_{i}_{j}')

    for i in range(9):
        model.AddAllDifferent([grid[(i, j)] for j in range(9)])
        model.AddAllDifferent([grid[(j, i)] for j in range(9)])

    for box_i in range(3):
        for box_j in range(3):
            box = [grid[(i, j)]
                   for i in range(box_i * 3, (box_i + 1) * 3)
                   for j in range(box_j * 3, (box_j + 1) * 3)]
            model.AddAllDifferent(box)

    for i in range(9):
        for j in range(9):
            val = 0 if puzzle[i * 9 + j] == '.' else int(puzzle[i * 9 + j])
            if val != 0:
                model.Add(grid[(i, j)] == val)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        return ''.join(str(solver.Value(grid[(i, j)])) for i in range(9) for j in range(9))
    return None

def main():
    puzzles = parse_puzzles('sudoku_input.txt')
    for puzzle in puzzles:
        start = time.time()
        solved = solve_sudoku(puzzle)
        end = time.time()
        print(solved)
        print("Solved in:", end - start, "seconds")

main()
