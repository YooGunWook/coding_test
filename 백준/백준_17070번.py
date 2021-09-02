import collections

n = int(input())
mat = []
visited = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)
    visited.append([0] * n)


def dfs(mat, n):  # dfs로 n,n에 갈 수 있는 모든 경우의 수 탐색
    stack = collections.deque([[(0, 0), (0, 1)]])
    # 각 케이스별 가능한 움직임
    row_f, row_t = [(0, 1), (0, 1)], [(0, 1), (1, 1)]
    col_f, col_t = [(1, 0), (1, 0)], [(1, 0), (1, 1)]
    cr_f, cr_t = [(1, 1), (1, 1), (1, 1)], [(0, 1), (1, 0), (1, 1)]
    while stack:  # stack이 없어질 때 까지 진행
        f, t = stack.pop()
        if f == (n - 1, n - 1) or t == (n - 1, n - 1):
            continue
        if f[0] == t[0]:  # row 케이스
            for idx in range(2):
                nf = (f[0] + row_f[idx][0], f[1] + row_f[idx][1])
                nt = (t[0] + row_t[idx][0], t[1] + row_t[idx][1])
                if idx == 0:
                    if (
                        0 <= nf[0] < n
                        and 0 <= nf[1] < n
                        and 0 <= nt[0] < n
                        and 0 <= nt[1] < n
                        and mat[nt[0]][nt[1]] != 1
                    ):
                        stack.append([nf, nt])
                        visited[nf[0]][nf[1]] += 1
                        visited[nt[0]][nt[1]] += 1
                elif idx == 1:
                    if (
                        0 <= nf[0] < n
                        and 0 <= nf[1] < n
                        and 0 <= nt[0] < n
                        and 0 <= nt[1] < n
                        and mat[nt[0]][nt[1]] != 1
                        and mat[nf[0]][nf[1] + 1] != 1
                        and mat[nf[0] + 1][nf[1]] != 1
                    ):
                        stack.append([nf, nt])
                        # visited[nf[0]][nf[1]] += 1
                        visited[nt[0]][nt[1]] += 1

        elif f[1] == t[1]:  # column 케이스
            for idx in range(2):
                nf = (f[0] + col_f[idx][0], f[1] + col_f[idx][1])
                nt = (t[0] + col_t[idx][0], t[1] + col_t[idx][1])
                if idx == 0:
                    if (
                        0 <= nf[0] < n
                        and 0 <= nf[1] < n
                        and 0 <= nt[0] < n
                        and 0 <= nt[1] < n
                        and mat[nt[0]][nt[1]] != 1
                    ):
                        stack.append([nf, nt])
                        # visited[nf[0]][nf[1]] += 1
                        visited[nt[0]][nt[1]] += 1
                elif idx == 1:
                    if (
                        0 <= nf[0] < n
                        and 0 <= nf[1] < n
                        and 0 <= nt[0] < n
                        and 0 <= nt[1] < n
                        and mat[nt[0]][nt[1]] != 1
                        and mat[nf[0]][nf[1] + 1] != 1
                        and mat[nf[0] + 1][nf[1]] != 1
                    ):
                        stack.append([nf, nt])
                        # visited[nf[0]][nf[1]] += 1
                        visited[nt[0]][nt[1]] += 1

        elif f[0] != t[0] and f[1] != t[1]:  # cross 케이스
            for idx in range(3):
                nf = (f[0] + cr_f[idx][0], f[1] + cr_f[idx][1])
                nt = (t[0] + cr_t[idx][0], t[1] + cr_t[idx][1])
                if idx == 0 or idx == 1:
                    if (
                        0 <= nf[0] < n
                        and 0 <= nf[1] < n
                        and 0 <= nt[0] < n
                        and 0 <= nt[1] < n
                        and mat[nt[0]][nt[1]] != 1
                    ):
                        stack.append([nf, nt])
                        # visited[nf[0]][nf[1]] += 1
                        visited[nt[0]][nt[1]] += 1
                elif idx == 2:
                    if (
                        0 <= nf[0] < n
                        and 0 <= nf[1] < n
                        and 0 <= nt[0] < n
                        and 0 <= nt[1] < n
                        and mat[nt[0]][nt[1]] != 1
                        and mat[nf[0]][nf[1] + 1] != 1
                        and mat[nf[0] + 1][nf[1]] != 1
                    ):
                        stack.append([nf, nt])
                        # visited[nf[0]][nf[1]] += 1
                        visited[nt[0]][nt[1]] += 1
    return visited


if mat[n - 1][n - 1] == 1:  # 끝이 1이면 뭘 해도 안되는 케이스임
    print(0)
print(dfs(mat, n)[n - 1][n - 1])
