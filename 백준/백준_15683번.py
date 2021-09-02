import collections
import copy

n, m = map(int, input().split(" "))
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)
cctv = []
block = []

for i in range(n):
    for j in range(m):
        if mat[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([i, j])
print(cctv)


def count_zero(mat):
    count = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                count += 1
    return count


def solution(mat):
    res = 0
    for i, j in cctv:
        if mat[i][j] == 1:
            dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
            min_count = 1000000000
            for idx in range(4):
                tmp_mat = copy.deepcopy(mat)
                nx, ny = i + dx[idx], j + dy[idx]
                while (0 <= nx < n) and (0 <= ny < m):
                    if tmp_mat[nx][ny] == 6:
                        break
                    elif tmp_mat[nx][ny] in [1,2,3,4,5]:
                        if dx[idx] == -1 and dy[idx] == 0:
                            nx -= 1
                        elif dx[idx] == 1 and dy[idx] == 0:
                            nx += 1
                        elif dx[idx] == 0 and dy[idx] == -1:
                            ny -= 1
                        elif dx[idx] == 0 and dy[idx] == 1:
                            ny += 1
                        continue
                    
                    tmp_mat[nx][ny] = 7
                    if dx[idx] == -1 and dy[idx] == 0:
                        nx -= 1
                    elif dx[idx] == 1 and dy[idx] == 0:
                        nx += 1
                    elif dx[idx] == 0 and dy[idx] == -1:
                        ny -= 1
                    elif dx[idx] == 0 and dy[idx] == 1:
                        ny += 1
                        
                zero = count_zero(tmp_mat)
                if min_count < zero:
                    
                
                

        if mat[i][j] == 2:
            if dx[idx] == -1:
                nx, ny = i + dx[idx], j + dy[idx]
                ncx, ncy = i + 1, j + dy[idx]
            elif dx[idx] == 1:
                continue
            elif dy[idx] == -1:
                nx, ny = i + dx[idx], j + dy[idx]
                ncx, ncy = i + dx[idx], j + 1
            elif dy[idx] == 1:
                continue

            while (0 <= nx < n) and (0 <= ny < m):
                if tmp_mat[nx][ny] == 6:
                    break
                tmp_mat[nx][ny] = 7
                if dx[idx] == -1 and dy[idx] == 0:
                    nx -= 1
                elif dx[idx] == 0 and dy[idx] == -1:
                    ny -= 1

            while (0 <= ncx < n) and (0 <= ncy < m):
                if tmp_mat[ncx][ncy] == 6:
                    break
                tmp_mat[ncx][ncy] = 7
                if dx[idx] == -1 and dy[idx] == 0:
                    ncx += 1
                elif dx[idx] == 0 and dy[idx] == -1:
                    ncy += 1

        if mat[i][j] == 3:
            if dx[idx] == -1:
                nx, ny = i + dx[idx], j + dy[idx]
                ncx, ncy = i + 1, j + dy[idx]
            elif dx[idx] == 1:
                continue
            elif dy[idx] == -1:
                nx, ny = i + dx[idx], j + dy[idx]
                ncx, ncy = i + dx[idx], j + 1
            elif dy[idx] == 1:
                continue
            while 0 <= nx < n or 0 <= ny < m:
                if tmp_mat[nx][ny] == 6:
                    break
                tmp_mat[nx][ny] = "#"
                if dx[idx] == -1 and dy[idx] == 0:
                    nx -= 1
                elif dx[idx] == 1 and dy[idx] == 0:
                    nx += 1
                elif dx[idx] == 0 and dy[idx] == -1:
                    ny -= 1
                elif dx[idx] == 0 and dy[idx] == 1:
                    ny += 1

        if mat[i][j] == 4:
            while 0 <= nx < n or 0 <= ny < m:
                if tmp_mat[nx][ny] == 6:
                    break
                tmp_mat[nx][ny] = "#"
                if dx[idx] == -1 and dy[idx] == 0:
                    nx -= 1
                elif dx[idx] == 1 and dy[idx] == 0:
                    nx += 1
                elif dx[idx] == 0 and dy[idx] == -1:
                    ny -= 1
                elif dx[idx] == 0 and dy[idx] == 1:
                    ny += 1

        if mat[i][j] == 5:
            while 0 <= nx < n or 0 <= ny < m:
                if tmp_mat[nx][ny] == 6:
                    break
                tmp_mat[nx][ny] = "#"
                if dx[idx] == -1 and dy[idx] == 0:
                    nx -= 1
                elif dx[idx] == 1 and dy[idx] == 0:
                    nx += 1
                elif dx[idx] == 0 and dy[idx] == -1:
                    ny -= 1
                elif dx[idx] == 0 and dy[idx] == 1:
                    ny += 1
        min_count = min(min_count, count_zero(tmp_mat))
    for i in tmp_mat:
        print(i)
    print()


print(solution(mat))
