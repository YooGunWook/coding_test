def solution(board, moves):
    tmp_res = []  # 인형을 담을 리스트
    answer = 0  # 정답
    for move in moves:  # 집게 움직임
        for i in range(len(board)):  # 각 행별로 확인해야함
            if board[i][move - 1] != 0:  # 0이 아니면 인형이 있다는 얘기
                tmp_res.append(board[i][move - 1])  # 인형 담을 리스트에 추가
                board[i][move - 1] = 0  # 인형을 담으면 해당 부분은 0으로 처리
                break
        if len(tmp_res) > 1:  # 1 이상일 때부터 2개 이상으로 연속되는 케이스 생김
            if tmp_res[-1] == tmp_res[-2]:
                tmp_res.pop()  # pop을 통해 없애준다. O(1)로 해결 가능
                tmp_res.pop()
                answer += 2  # 2개가 없어졌으니 2개 더해준다.
    return answer


board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))