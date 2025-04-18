import sys
from collections import deque
import time

def parse_puzzles(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def print_puzzle(puzzle):
    for i in range(0, 81, 9):
        print("".join(puzzle[i:i+9]))

def ac3(domains, neighbors):
    queue = deque([(xi, xj) for xi in domains for xj in neighbors[xi]])
    while queue:
        xi, xj = queue.popleft()
        if revise(domains, xi, xj):
            if not domains[xi]:
                return False
            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def revise(domains, xi, xj):
    revised = False
    for x in set(domains[xi]):
        if not any(x != y for y in domains[xj]):
            domains[xi].remove(x)
            revised = True
    return revised

def backtrack(assignment, domains, neighbors):
    if all(len(domains[cell]) == 1 for cell in domains):
        return {cell: domains[cell][0] for cell in domains}

    cell = min((c for c in domains if len(domains[c]) > 1), key=lambda c: len(domains[c]))
    for value in domains[cell]:
        new_domains = {c: list(domains[c]) for c in domains}
        new_domains[cell] = [value]
        if ac3(new_domains, neighbors):
            result = backtrack(assignment, new_domains, neighbors)
            if result:
                return result
    return None

def sudoku_csp_solver(puzzle):
    digits = '123456789'
    cells = [r + c for r in 'ABCDEFGHI' for c in digits]
    values = dict(zip(cells, puzzle))
    domains = {cell: [int(values[cell])] if values[cell] != '.' else list(range(1, 10)) for cell in cells}

    units = []
    for r in 'ABCDEFGHI':
        units.append([r + c for c in digits])
    for c in digits:
        units.append([r + c for r in 'ABCDEFGHI'])
    for rs in ('ABC','DEF','GHI'):
        for cs in ('123','456','789'):
            units.append([r + c for r in rs for c in cs])

    neighbors = {cell: set(sum([u for u in units if cell in u], [])) - {cell} for cell in cells}

    if not ac3(domains, neighbors):
        return None

    result = backtrack({}, domains, neighbors)
    if result:
        return ''.join(str(result[cell]) for cell in cells)
    return None

def main():
    puzzles = parse_puzzles('sudoku_input.txt')
    for puzzle in puzzles:
        start = time.time()
        solved = sudoku_csp_solver(puzzle)
        end = time.time()
        print(solved)
        print("Solved in:", end - start, "seconds")

if __name__ == "__main__":
    main()
