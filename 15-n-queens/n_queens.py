def dfs_n_queens(n: int) -> list:
    if n < 1:
        return []

    solutions = []
    # a queen at (row, col) owns the whole diagonal row - col and anti-diagonal
    # row + col, so one integer per diagonal replaces a list of attacked squares
    stack = [(0, [], set(), set(), set())]

    while stack:
        row, placed, cols, diagonals, anti_diagonals = stack.pop()

        if row == n:
            solutions.append(placed)
            continue

        for col in reversed(range(n)):
            if col in cols or row - col in diagonals or row + col in anti_diagonals:
                continue
            stack.append((
                row + 1,
                placed + [col],
                cols | {col},
                diagonals | {row - col},
                anti_diagonals | {row + col},
            ))

    return sorted(solutions)


if __name__ == "__main__":
    print(dfs_n_queens(4))
