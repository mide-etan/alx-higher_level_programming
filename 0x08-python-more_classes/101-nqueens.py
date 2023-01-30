import sys

def nqueens(n):
    def is_not_under_attack(row, col, queens):
        for (r, c) in queens:
            if r == row or c == col or \
               abs(row-r) == abs(col-c):
                return False
        return True

    def solve(n, row, queens, results):
        if row == n:
            results.append(queens)
            return

        for col in range(n):
            if is_not_under_attack(row, col, queens):
                solve(n, row+1, queens + [(row, col)], results)

    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    results = []
    solve(n, 0, [], results)

    for solution in results:
        print(" ".join(". "*c + "Q " + ". "*(n-c-1) for (r, c) in solution))

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

nqueens(sys.argv[1])
