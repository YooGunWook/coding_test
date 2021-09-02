from itertools import combinations
import sys

n = int(input())

mat = []
for _ in range(n):
    row = input().split(" ")
    mat.append(row)

empty = []
teacher = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == "X":
            empty.append((i, j))
            continue
        if mat[i][j] == "T":
            teacher.append((i, j))
            continue

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def solution():
    for obj in combinations(empty, 3):
        for x, y in obj:
            mat[x][y] = "O"

        flag = False
        for t in teacher:
            for i in range(4):
                x, y = t
                while 0 <= x < n and 0 <= y < n and mat[x][y] != "O":
                    if mat[x][y] == "S":
                        flag = True
                        break
                    x += dx[i]
                    y += dy[i]
                if flag:
                    break
            if flag:
                break

        if not flag:
            print("YES")
            return

        for x, y in obj:
            mat[x][y] = "X"
    print("NO")


solution()