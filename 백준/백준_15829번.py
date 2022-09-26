from string import ascii_lowercase

l = int(input())
st = input()
r = 31
m = 1234567891

# 이걸 ord()로 하는게 좋을 듯. -> ord("a") - 96
alpha_dict = {a: idx + 1 for idx, a in enumerate(ascii_lowercase)}


def hash_function(alpha_dict, st, r, m, l):
    h = 0  # longtype 변환
    for idx in range(l):  # O(n)
        h += alpha_dict[st[idx]] * (r ** idx) % m
    return h % m


print(hash_function(alpha_dict, st, r, m, l))
