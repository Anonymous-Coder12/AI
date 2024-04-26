def isSafe(board, row, col, n):
    rowDup = row
    colDup = col
    while row >= 0 and col >= 0:
        if (board[row][col] == 'Q'):
            return False
        row -= 1
        col -= 1
    row = rowDup
    col = colDup
    if ('Q' in board[row]):
        return False
    while row < n and col >= 0:
        if (board[row][col] == 'Q'):
            return False
        row += 1
        col -= 1
    return True


def solve(col, n, ans, board):
    if col == n:
        y = [x for x in board]
        ans.append(y)
        return
    for row in range(n):

        if isSafe(board, row, col, n) == True:
            x = board[row]
            s = board[row][0:col]
            s = s+'Q'
            s = s+board[row][col+1:]
            board[row] = s

            solve(col+1, n, ans, board)
            board[row] = x


def solveNQueens(n):
    ans = []
    board = []
    s = "."*n
    for i in range(n):
        board.append(s)

    solve(0, n, ans, board)
    return ans


n = int(input("enter n:"))
arr = solveNQueens(n)
for i in range(len(arr)):
    print(i+1)
    for j in range(len(arr[i])):
        print(arr[i][j])
