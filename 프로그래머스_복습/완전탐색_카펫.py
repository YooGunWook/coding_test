def solution(brown, yellow):
    s = brown + yellow
    target = []
    for i in range(1, s + 1):
        if s % i == 0:
            target.append([i, s // i])
    for t in target:
        if t[0] < 2 or t[1] < 2:
            continue
        if t[0] < t[1]:
            continue
        y = (t[0] - 2) * (t[1] - 2)
        b = s - y
        if y == yellow and b == brown:
            return t


if __name__ == "__main__":
    brown = 10
    yellow = 2
    print(solution(brown, yellow))
