import copy
import collections

s = input()
count = 0
char_count = collections.Counter(s)
for key in char_count:
    tmp_char_count = copy.deepcopy(char_count)
    tmp_char = [key] * len(s)
    tmp_char_count[key] -= 1
    ## tmp_char, tmp_char_count, idx
    
    for i in range(1, len(s) - 1):
        for key in char_count:
            if tmp_char[i-1] != key and tmp_char_count[key] != 0:
                tmp_char[i] = key
                tmp_char_count[key] -= 1
    if sum(tmp_char_count.values()) == 0:
        count += 1
print(count)


def is_lucky(tmp_char, tmp_char_count, idx):
    for i in range(idx, len(s) - 1):
        for key in char_count:
            if tmp_char[i-1] != key and tmp_char_count[key] != 0:
                tmp_char[i] = key
                tmp_char_count[key] -= 1