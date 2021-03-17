k = int(input())


def mos(n):
    for i in range(len(n)):
        if n[i] == "0":
            n += "1"
        elif n[i] == "1":
            n += "0"
        if len(n) == k:
            return n[k - 1]
    return mos(n)


print(mos("0"))
