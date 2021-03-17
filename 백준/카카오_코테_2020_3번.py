def turnkey(key):
    row = len(key)
    col = len(key[0])
    mat = []
    for _ in range(row):
        r = [0] * col
        mat.append(r)
    for i in range(row):
        for j in range(col):
            mat[j][row - i - 1] = key[i][j]
    return mat


def attach(x, y, m, key, board):
    for i in range(m):
        for j in range(m):
            board[x + i][y + j] += key[i][j]


def detach(x, y, m, key, board):
    for i in range(m):
        for j in range(m):
            board[x + i][y + j] -= key[i][j]


def check(board, m, n):
    for i in range(n):
        for j in range(n):
            if board[m + i][m + j] != 1:
                return False
    return True


def solution(key, lock):
    m, n = len(key), len(lock)
    board = [[0] * (m * 2 + n) for _ in range(m * 2 + n)]
    for i in range(n):
        for j in range(n):
            board[m + i][m + j] = lock[i][j]

    for _ in range(4):
        key = turnkey(key)
        for x in range(1, m + n):
            for y in range(1, m + n):
                attach(x, y, m, key, board)
                if check(board, m, n):
                    return True
                detach(x, y, m, key, board)
    return False