def find_square(m,n,board):
    check_list = [[0]*n for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            if board[i][j] == board[i][j-1] == board[i-1][j] == board[i-1][j-1] != 0:
                check_list[i][j] = 1
                check_list[i-1][j] = 1
                check_list[i][j-1] = 1
                check_list[i-1][j-1] = 1
    return check_list


def delete_value(m,n,board,check_list):
    for i in range(m):
        for j in range(n):
            if check_list[i][j] == 1:
                board[i][j] = 0
    return board


def fall(m,n,board):
    for i in range(n):
        for j in range(m-1):
            if board[j][i] == 0:
                continue
            if board[j+1][i] == 0:
                count_fall = 0
                change_row = 0
                while j+1+count_fall <= m-1:
                    if board[j+1 + count_fall][i] == 0:
                        count_fall += 1
                    else:
                        break
                while j - change_row >= 0:
                    board[j+count_fall-change_row][i] = board[j-change_row][i]
                    board[j-change_row][i] = 0
                    change_row += 1
    return board

def solution(m,n,board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    
    count = []
    while 1:
        a = find_square(m,n,board)
        b = delete_value(m,n,board, a)
        fall(m,n,b)
        temp = 0
        for i in b:
            temp += i.count(0)
        count.append(temp)
        if len(count)>1 and count[-1]==count[-2] :
            break
            
    return count[-1]