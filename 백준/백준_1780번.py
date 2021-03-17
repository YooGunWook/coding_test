n = int(input())
mat = []
for _ in range(n):
    row = list(input().split(" "))
    mat.append(row)

zero = 0
one = 0
minus = 0


def divide_con(x, y, n):
    global zero, one, minus
    typ = mat[y][x]
    double_break = False

    for i in range(x, x + n):
        if double_break:
            break
        for j in range(y, y + n):
            if mat[j][i] != typ:
                divide = n // 3
                divide_con(x, y, divide)
                divide_con(x, y + divide, divide)
                divide_con(x, y + divide + divide, divide)
                divide_con(x + divide, y, divide)
                divide_con(x + divide + divide, y, divide)
                divide_con(x + divide, y + divide, divide)
                divide_con(x + divide + divide, y + divide, divide)
                divide_con(x + divide, y + divide + divide, divide)
                divide_con(x + divide + divide, y + divide + divide, divide)

                double_break = True
                break
    if not double_break:
        if mat[y][x] == "-1":
            minus += 1
        elif mat[y][x] == "0":
            zero += 1
        elif mat[y][x] == "1":
            one += 1


divide_con(0, 0, n)
print(minus)
print(zero)
print(one)