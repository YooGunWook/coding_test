def friends(m, n, board, visited):
    for i in range(m-1):
        for j in range(1, n):
            if board[i][j] != ' ' and board[i][j] == board[i][j-1] and board[i][j-1:j+1] == board[i+1][j-1:j+1]:
                    visited[i][j] = True
                    visited[i][j-1] = True
                    visited[i+1][j] = True
                    visited[i+1][j-1] = True
    
def deleteBlock(m, n, board, visited):
    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j] == True:
                cnt += 1
                board[i] = board[i][:j] + ' ' + board[i][j+1:]
    
    rotation_board = []
    for i in range(n):
        tmp = ''
        for j in range(m):
            tmp += board[j][i]
        rotation_board.append(tmp)
        
    for i in range(n):
        for j in range(1, m):
            if rotation_board[i][j] == ' ':
                rotation_board[i] = ' ' + rotation_board[i][:j] + rotation_board[i][j+1:]
    
    tmp_board = []
    for i in range(m):
        tmp = ''
        for j in range(n):
            tmp += rotation_board[j][i]
        tmp_board.append(tmp)
        
    board = tmp_board
    
    return board, cnt
    
def solution(m, n, board):
    answer = 0
    result = 1
    while result:
        visited = [[False] * n for _ in range(m)]
        friends(m, n, board, visited)
        board, result = deleteBlock(m, n, board, visited)
        answer += result
    return answer