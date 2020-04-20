def solution(board):
    # max_point를 0으로 지정
    max_point = 0
    # 이걸 해주는 이유: 초기에 정사각형이 만들어지는 환경이 아니라면 계산을 끝내기 위해
    for i in range(0,len(board)):
        max_point += sum(board[i][:])
    if max_point == 0:
        return 0
    # 만약 만들 수 있는 환경이라면 다시 0부터 시작
    max_point = 0

    # 제일 윗줄과 첫번째 col은 정사각형 만들 때 필요 없기 때문에 1부터 시작
    for i in range(1, len(board)):
        for j in range(1,len(board[0])):
            # board[i][j]가 0이라면 정사각형이 만들어지지 않기 때문에 생략
            if board[i][j] == 0:
                continue
            # 최솟점을 찾는 이유는 최솟점을 통해 최대 정사각형을 구할 수 있기 때문.
            min_point = min(board[i-1][j],board[i][j-1],board[i-1][j-1])
            # 이런식으로 최솟점에 1을 더해주면 최대 정사각형 크기가 나온다.
            min_point += 1
            # 메모이제이션을 위해 해당 값에 최솟점을 넣어준다. 
            board[i][j] = min_point
            # max_point가 최솟점보다 작으면 max_point를 갱신해준다.
            if max_point < board[i][j]:
                max_point = board[i][j]
    # max_point가 0이면 최대 정사각형의 크기가 1이므로 1을 리턴한다.
    if max_point == 0:
        return 1
    # max_point가 0이 아니면 max_point에 제곱을 해준다. 
    else:
        return max_point ** 2