def solution(sizes):
    answer = 0
    n = len(sizes)

    # 가장 큰 지갑 사이즈
    m_big = 0
    m_small = 0

    # O(n)으로 조회
    for i in range(n):

        big = sizes[i][0]
        small = sizes[i][1]

        # small이 더 작을 때 
        # 큰건 큰거끼리, 작은건 작은거 끼리
        # 하면 자연스럽게 가장 적절한 값이 나온다.
        if big < small:
            temp = big
            big = small
            small = temp

        # 큰 값 업데이트
        if big > m_big:
            m_big = big

        # 작은 값 업데이트
        if small > m_small:
            m_small = small

    answer = m_small * m_big

    return answer


sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(sizes))