n = int(input())
mat = []
for _ in range(n):
    mat.append(list(input().split(" ")))

zero = 0
one = 0


def divide_conc(x, y, n):
    global zero, one
    flag = False
    typ = mat[y][x]
    for i in range(x, x + n):
        if flag:
            break
        for j in range(y, y + n):
            if mat[j][i] != typ:
                divide = n // 2
                divide_conc(x, y, divide)
                divide_conc(x + divide, y, divide)
                divide_conc(x, y + divide, divide)
                divide_conc(x + divide, y + divide, divide)
            
                flag = True
                break
    if not flag:
        if mat[y][x] == '0':
            zero += 1
        elif mat[y][x] == '1':
            one += 1
            

divide_conc(0,0,n)