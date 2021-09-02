def solution(X, Y):
    low, high = 1, 1000000000  # 최저 횟수와 최대 횟수
    Z = int(Y * 100 / X)  # 승률
    if Z >= 99:
        return -1

    while low < high:  # low가 더 커질때까지 반복
        mid = (low + high) // 2
        tx, ty = mid + X, mid + Y  # mid를 할 예정인 count로 생각
        tz = int(ty * 100 / tx)  # 새로운 승률
        if Z >= tz:  # 이게 Z보다 작으면 low에 1씩 더하고, 더 크면 high는 mid로 처리한다
            low = mid + 1
        else:
            high = mid  # 이때 쯤 되면 반복문이 끝남
    return high


if __name__ == "__main__":
    print(solution(1000000000, 470000000))