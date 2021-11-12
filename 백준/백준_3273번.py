n = int(input())
num_list = list(map(int, input().split(" ")))
x = int(input())

# 투 포인터 기반 풀이
def solution(num_list, n, x):
    count = 0
    left = 0  # list의 처음
    right = n - 1  # list의 끝
    if n == 1:  # list의 길이가 1이면 무조건 0이다.
        return 0
    # 정렬을 통해 투포인터 계산할 수 있게 만듦.
    num_list = sorted(num_list)
    while left < right:  # left가 right보다 작을때까지만 반복
        left_val = num_list[left]
        right_val = num_list[right]
        sum_val = left_val + right_val
        if sum_val == x:  # 같을 경우에는 right를 하나 줄인다.
            count += 1
            right -= 1
        elif sum_val < x:  # 더 작을 경우 left를 하나 늘린다.
            left += 1
        elif sum_val > x:  # 더 클 경우 right를 하나 줄인다.
            right -= 1

    return count


print(solution(num_list, n, x))
