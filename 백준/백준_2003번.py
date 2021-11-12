n, m = list(map(int, input().split(" ")))
num_list = list(map(int, input().split(" ")))

# 투 포인터 기반 풀이
def solution(num_list, n, m):
    left = 0  # 왼쪽 포인터
    tmp_num = num_list[left]  # 임시 값
    count = 0

    # 만약 리스트의 길이가 1일 때
    if n == 1:
        if num_list[0] == m:
            return 1
        else:
            return 0

    # right를 계속 옮기는 방식으로 진행
    for right in range(1, n):
        tmp_num += num_list[right]
        if tmp_num == m:  # 동일한 값이 나올 때
            count += 1
        elif tmp_num > m:  # 다 더했을 때 더 큰 값이 나올 때
            while True:
                # left를 하나씩 늘린다.
                tmp_num -= num_list[left]
                left += 1
                if tmp_num == m:  # 동일한 값이 나올 때
                    count += 1
                    break
                elif tmp_num < m:  # 더 적은 값이 나올 때
                    break
                elif left == right:  # left랑 right가 같아질 때
                    break
    return count


print(solution(num_list, n, m))

