def kan(value):
    if value == 1:
        return "-"
    else:
        return kan(int(value / 3)) + " " * int(value / 3) + kan(int(value / 3))


while True:
    try:
        value = 3 ** int(input())
        print(kan(value))
    except:
        break