import itertools


def nonDivisibleSubset(k, s):
    remainder = [S % k for S in s]
    result = 0
    for i in range(1, k // 2 + 1):
        if i != k - i:
            result += max(remainder.count(i), remainder.count(k - i))
        else:
            result += int(bool(remainder.count(i)))
    result += int(bool(remainder.count(0)))
    return result


k = 7
s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
print(nonDivisibleSubset(k, s))
