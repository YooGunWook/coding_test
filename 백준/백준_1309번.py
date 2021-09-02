n = int(input())
no_lion, left_lion, right_lion = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
val = 9901

no_lion[0] = 1  # 사자를 한마리도 배치 안했을 때 케이스
for i in range(1, n + 1):  # 그 이후 케이스
    no_lion[i] = (
        no_lion[i - 1] + left_lion[i - 1] + right_lion[i - 1]
    ) % val  # 해당 줄에 사자를 아무도 배치 안했을 때 케이스
    left_lion[i] = (no_lion[i - 1] + right_lion[i - 1]) % val  # 해당 줄의 왼쪽에 사자를 배치했을 때
    right_lion[i] = (no_lion[i - 1] + left_lion[i - 1]) % val  # 해당 줄의 오른쪽에 사자를 배치했을 때
    # % val은 메모리 관련 이슈 때문에 필요함.
    # 최종적으로는 나머지를 계산하기 위한 것도 있음.
print((no_lion[n] + left_lion[n] + right_lion[n]) % val)