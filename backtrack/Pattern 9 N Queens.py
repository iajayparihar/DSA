"""
Backtracking pattern: N Queens

Idea:
- Place one queen per row and try all columns while avoiding attacks on rows, columns, and diagonals.
- When a full board is formed, record the solution.

Why it works:
- Each recursive level places a queen in a safe position so that every final board satisfies the puzzle rules.
- The sets for columns and diagonals guarantee that no two queens attack each other.

Time Complexity:
- The search explores permutations of rows and columns, which is roughly O(n!) in the worst case.
- Each state checks attack conditions in O(1) time.

Space Complexity:
- The board and the three sets use O(n^2) and O(n) space respectively.
- Extra space excluding output: O(n^2) for the board, or O(n) for the search state alone.
"""

n=4

board=[["."]*n for _ in range(n)]

cols=set()
diag1=set()
diag2=set()

def backtrack(row):

    if row==n:
        for r in board:
            print(r)
        print()
        return

    for col in range(n):

        if col in cols:
            continue

        if row-col in diag1:
            continue

        if row+col in diag2:
            continue

        cols.add(col)
        diag1.add(row-col)
        diag2.add(row+col)

        board[row][col]="Q"

        backtrack(row+1)

        board[row][col]="."

        cols.remove(col)
        diag1.remove(row-col)
        diag2.remove(row+col)

backtrack(0)