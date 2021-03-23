# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, Y, D):
    target = Y - X
    count = target // D
    if target % D == 0:
        return count
    else:
        return count + 1


print(solution(10, 85, 30))
