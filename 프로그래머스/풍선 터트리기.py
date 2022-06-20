# 투포인터 기반 풀이
def solution(a):
    answer = 1 
    left, right = 0, len(a) - 1
    lmin = a[0]
    rmin = a[-1]

    # 두개의 포인터 중 큰 값을 찾고
    # 그 다음에 옆에 인접한 값보다 큰지 작은지 체크
    # 크면 정답에 + 1 작으면 - 1
    while left < right:
        if lmin > rmin:
            left += 1

            if a[left] < lmin:
                answer += 1
                lmin = a[left]

        elif lmin < rmin:
            right -= 1
            if a[right] < rmin:
                answer += 1
                rmin = a[right]

    return answer


print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))