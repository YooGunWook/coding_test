h, w, x, y = list(map(int, input().split(" ")))

mat = []
for _ in range(h + x):
    row = list(map(int, input().split(" ")))
    mat.append(row)

a_mat = []
for _ in range(h):
    row = [0] * w
    a_mat.append(row)
for i in range(h + x):
    for j in range(w + y):
        if mat[i][j] == 0:
            continue
        if 0 <= i < h and 0 <= j < w:
            if i - x < 0 or j - y < 0:
                a_mat[i][j] = mat[i][j]
                continue
            a_mat[i][j] = mat[i][j] - a_mat[i-x][j-y]
            continue
        
for row in a_mat:
    row = [str(i) for i in row]
    print(" ".join(row))