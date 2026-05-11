def safe(board, r, c, n):
    for i in range(r):
        if board[i][c] == 'Q':
            return False

    i, j = r, c
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i, j = r, c
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
 
    return True

def solve(board, r, n):
    if r == n:
        return True

    for c in range(n):
        if safe(board, r, c, n):
            board[r][c] = 'Q'

            if solve(board, r + 1, n):
                return True

            board[r][c] = '.'

    return False


def nQueen(n):
    board = [['.' for _ in range(n)] for _ in range(n)]

    if solve(board, 0, n):
        for row in board:
            print(" ".join(row))
    else:
        print("No solution")


nQueen(int(input("Enter number of queens: ")))

########################################################################

def solve(i, cols, ld, rd, cur, n):
    if i == n: return True
    for j in range(n):
        if cols[j] or rd[i+j] or ld[i-j+n-1]: continue
        cols[j] = rd[i+j] = ld[i-j+n-1] = 1
        cur.append(j)
        if solve(i+1, cols, ld, rd, cur, n): return True
        cur.pop()
        cols[j] = rd[i+j] = ld[i-j+n-1] = 0
    return False

def nQueen(n):
    cols, ld, rd, cur = [0]*n, [0]*(2*n), [0]*(2*n), []
    if solve(0, cols, ld, rd, cur, n):
        b = [['.']*n for _ in range(n)]
        for i in range(n): b[i][cur[i]] = 'Q'
        for row in b: print(" ".join(row))
    else: print("No solution exists.")

nQueen(int(input("Enter the number of queens:\t")))