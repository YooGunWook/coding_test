def solution(n, lost, reserve):
    answer = 0
    _reserve = sorted([r for r in reserve if r not in lost])
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        b = r - 1
        f = r + 1
        if b in _lost:
            _lost.remove(b)
        elif f in _lost:
            _lost.remove(f)
    return n - len(_lost)


if __name__ == "__main__":
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]
    solution(n, lost, reserve)
