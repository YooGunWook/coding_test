import pprint

n = 8
m = 7
matrix = [
    [4, 3, 2, 2, 1, 0, 1],
    [3, 3, 3, 2, 1, 0, 1],
    [2, 2, 2, 2, 1, 0, 0],
    [2, 1, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 1, 2, 2, 1, 1, 0],
    [0, 1, 1, 1, 2, 1, 0],
]

dir = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]


def dfs(matrix, i, j, visited):
    for k in range(len(dir)):
        y = i + dir[k][0]
        x = j + dir[k][1]

        if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[0]):
            continue
        if matrix[i][j] < matrix[y][x]:
            return False
        if visited[y][x] or matrix[i][j] != matrix[y][x]:
            continue
        visited[y][x] = True
        dfs(matrix, y, x, visited)


def solution(matrix, n, m):
    visited = []
    isPeak = True
    for _ in range(n):
        visited.append([False] * m)
    count = 0
    if not matrix:
        return count
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                isPeak = True
                result = dfs(matrix, i, j, visited)
                if result == False:
                    print(i)
                    print(j)
                    isPeak = False
                if isPeak == True:
                    count += 1
    return count


if __name__ == "__main__":

    print(solution(matrix, n, m))
