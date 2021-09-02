n = int(input())
mat = []
for _ in range(n):
    row = list(input())
    mat.append(row)


def decompose(x, y, n):
    if n == 1:
        print(mat[y][x], end="")
        return
    flag = True
    for i in range(y, y + n):
        if not flag:
            break
        for j in range(x, x + n):
            if mat[i][j] != mat[y][x]:
                flag = False
                break
    if flag:
        print(mat[y][x], end="")
    else:
        decreased_n = n // 2

        print("(", end="")
        decompose(x, y, decreased_n)
        decompose(x + decreased_n, y, decreased_n)
        decompose(x, y + decreased_n, decreased_n)
        decompose(x + decreased_n, y + decreased_n, decreased_n)
        print(')', end='')
        
decompose(0,0,n)
