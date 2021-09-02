import sys

n, r, c = map(int, sys.stdin.readline().split(' '))
count = 0


def divide_con(x, y, n):
    global count
    
    if x == r and y == c:
        print(int(count))
        exit(0)

    if n == 1:
        count += 1
        return

    if not (x <= r < x + n and y <= c < y + n):
        count += n * n
        return

    divide_con(x, y, n / 2)
    divide_con(x, y + n / 2, n / 2)
    divide_con(x + n / 2, y, n / 2)
    divide_con(x + n / 2, y + n / 2, n / 2)


divide_con(0, 0, 2 ** n)
