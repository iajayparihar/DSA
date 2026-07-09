"""
Backtracking pattern: Word Search

Idea:
- Start from each cell and explore four directions while matching the next character of the word.
- The board cell is marked temporarily so the same cell is not reused in the same path.

Why it works:
- A path is valid only if every step matches the next character of the target word.
- Backtracking allows the search to try another route if one branch fails.

Time Complexity:
- At each cell, the search can branch into up to four directions and continue for L characters.
- Worst-case time is about O(m * n * 4 * 3^(L-1)) = O(m * n * 3^L) for an m x n board.

Space Complexity:
- The recursion depth is O(L), where L is the word length.
- The in-place board marking uses O(1) extra space apart from the recursion stack.
"""

board=[
['A','B','C'],
['D','E','F'],
['G','H','I']
]

word="ABE"

ROWS=len(board)
COLS=len(board[0])

def dfs(r,c,index):

    if index==len(word):
        return True

    if r<0 or c<0 or r>=ROWS or c>=COLS:
        return False

    if board[r][c]!=word[index]:
        return False

    temp=board[r][c]
    board[r][c]="#"

    found=(
        dfs(r+1,c,index+1) or
        dfs(r-1,c,index+1) or
        dfs(r,c+1,index+1) or
        dfs(r,c-1,index+1)
    )

    board[r][c]=temp

    return found