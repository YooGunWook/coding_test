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


def dfs(matrix, visited, i, j):
    if i < 0 or i >= len(matrix) - 1 or j < 0 or j >= len(matrix[0]) - 1:
        return

    if matrix[i][j] < matrix[i + 1][j] or matrix[i][j] < matrix[i - 1][j]:
        return False
    if matrix[i][j] < matrix[i][j + 1] or matrix[i][j] < matrix[i][j - 1]:
        return False
    if matrix[i][j] < matrix[i - 1][j - 1] or matrix[i][j] < matrix[i + 1][j + 1]:
        return False
    if matrix[i][j] < matrix[i - 1][j + 1] or matrix[i][j] < matrix[i + 1][j - 1]:
        return False

    if (
        visited[i + 1][j] == True
        or visited[i - 1][j] == True
        or visited[i][j - 1] == True
        or visited[i][j + 1] == True
        or visited[i - 1][j - 1] == True
        or visited[i + 1][j + 1] == True
        or visited[i - 1][j + 1] == True
        or visited[i + 1][j - 1] == True
        or matrix[i][j] != matrix[i + 1][j]
        or matrix[i][j] != matrix[i - 1][j]
        or matrix[i][j] != matrix[i][j + 1]
        or matrix[i][j] != matrix[i][j - 1]
        or matrix[i][j] != matrix[i - 1][j - 1]
        or matrix[i][j] != matrix[i + 1][j + 1]
        or matrix[i][j] != matrix[i - 1][j + 1]
        or matrix[i][j] != matrix[i + 1][j - 1]
    ):
        return

    visited[i][j] = True
    dfs(matrix, visited, i + 1, j)
    dfs(matrix, visited, i - 1, j)
    dfs(matrix, visited, i, j + 1)
    dfs(matrix, visited, i, j - 1)
    dfs(matrix, visited, i + 1, j + 1)
    dfs(matrix, visited, i + 1, j - 1)
    dfs(matrix, visited, i - 1, j - 1)
    dfs(matrix, visited, i - 1, j + 1)


def solution(matrix, n, m):
    visited = []
    for _ in range(n):
        visited.append([False] * m)
    count = 0
    if not matrix:
        return count

    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                isPeak = True
                result = dfs(matrix, visited, i, j)
                if result == False:
                    isPeak = False
                if isPeak:
                    visited[i][j] = True
                    print(visited)
                    count += 1
    return count


if __name__ == "__main__":
    print(solution(matrix, n, m))