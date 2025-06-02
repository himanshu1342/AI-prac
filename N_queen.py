def is_safe(queen_positions, row, col):
    for r in range(row):
        c = queen_positions[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_n_queens_util(n, row, queen_positions, solutions):
    if row == n:
        solutions.append(queen_positions[:])
        return

    for col in range(n):
        if is_safe(queen_positions, row, col):
            queen_positions[row] = col
            solve_n_queens_util(n, row + 1, queen_positions, solutions)

def solve_n_queens(n):
    solutions = []
    queen_positions = [-1] * n  # Index: row, Value: column
    solve_n_queens_util(n, 0, queen_positions, solutions)
    return solutions

def print_solutions(solutions):
    for index, solution in enumerate(solutions):
        print(f"\nSolution {index + 1}:")
        n = len(solution)
        for i in range(n):
            row = ['.'] * n
            row[solution[i]] = 'Q'
            print(' '.join(row))

# Example usage
n = 4
solutions = solve_n_queens(n)
print_solutions(solutions)
