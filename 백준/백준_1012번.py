T = int(input())
v = [int(value) for value in input().split(" ")]
M = v[0]
N = v[1]
K = v[2]
farm = [[0] * M for _ in range(N)]
for _ in range(K):
    loc = [int(value) for value in input().split(" ")]
    farm[loc[1]][loc[0]] = 1


def dfs(i, j, farm):
    if i < 0 or i >= len(farm) or j < 0 or j >= len(farm[0]) or farm[i][j] != 1:
        return
    farm[i][j] = 0

    # 동서남북 탐색
    dfs(i + 1, j, farm)
    dfs(i - 1, j, farm)
    dfs(i, j + 1, farm)
    dfs(i, j - 1, farm)


def solution(farm):
    count = 0
    for i in range(len(farm)):
        for j in range(len(farm[0])):
            if farm[i][j] == 1:
                dfs(i, j, farm)
                count += 1
    return count


print(farm)