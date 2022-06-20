import collections

# stack, queue 방식 활용
def solution(rows, columns, queries):
    mat = []
    answer = []
    row = []

    for i in range(1, (rows * columns) + 1):
        row.append(i)
        if len(row) == columns:
            mat.append(row)
            row = []

    # 회전 시키기
    for query in queries:
        x1, y1, x2, y2 = query
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        row = collections.deque([])

        # 우선 필요한 값들을 가져온다.
        for i in range(y1, y2 + 1):
            row.append(mat[x1][i])

        for i in range(x1 + 1, x2 + 1):
            row.append(mat[i][y2])

        for i in range(y2 - 1, y1 - 1, -1):
            row.append(mat[x2][i])

        for i in range(x2 - 1, x1, -1):
            row.append(mat[i][y1])

        # 정답
        answer.append(min(row))

        # 회전 시키기
        val = row.pop()
        row.appendleft(val)

        # 가져온 값들을 회전 시켜서 넣어준다.
        for i in range(y1, y2 + 1):
            val = row.popleft()
            mat[x1][i] = val

        for i in range(x1 + 1, x2 + 1):
            val = row.popleft()
            mat[i][y2] = val

        for i in range(y2 - 1, y1 - 1, -1):
            val = row.popleft()
            mat[x2][i] = val

        for i in range(x2 - 1, x1, -1):
            val = row.popleft()
            mat[i][y1] = val

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
