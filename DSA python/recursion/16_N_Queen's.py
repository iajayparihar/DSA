def isSafe(row,col,board,n):
    duprow = row
    dupcol = col
    # check for daigonal
    while row>=0 and col>=0: # upper left daigonal 
        if board[row][col] == "Q":
            return False
        row-=1 ; col -=1

    row = duprow
    col = dupcol
    while col>=0: #  left row
        if board[row][col] == "Q":
            return False
        col-=1

    row = duprow
    col = dupcol
    while row<n and col>=0: # bottom left daigonal
        if board[row][col] == "Q":
            return False
        row+=1 ; col -=1

    return True # if all false then 


def NQproblem(col, board, ans,n):
    if col == n:
        ans.append(board)
        print(ans)
        return 
    
    for row in range(4):
        if(isSafe(row,col,board,n)):
            board[row][col]="Q"
            NQproblem(col+1, board, ans, n)
            board[row][col]="."

    return ans

board=[["."]*4,["."]*4,["."]*4,["."]*4]
print(board)
ans = list()
a=NQproblem(0,board,ans, 4)
print(a)

