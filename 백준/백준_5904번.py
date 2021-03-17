n = int(input())


def get_char(n):
    if n == 0:
        return 'moo'
    else:
        return get_char(n-1) + 'm' + 'o'*(n+2) + get_char(n-1)

for i in range(n):
    if n <= 3:
        print(n)
        break
    sent = get_char(i)
    if len(sent) < n:
        continue
    if len(sent) >= n:
        print(sent[n-1])
        break