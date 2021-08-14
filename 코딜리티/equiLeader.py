# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections


def solution(A):
    """
    과반수이기 때문에 어차피 최대는 같다.
    """
    maxLeader = 0

    # 오른쪽 애들 정보
    rightCount = collections.Counter(A)
    rightLen = len(A)

    # 왼쪽 애들 정보
    leftCount = collections.defaultdict(int)
    leftLen = 0
    leftLeader = 0
    leaderCount = 0

    for val in A:  # 하나씩 조회
        rightCount[val] -= 1
        rightLen -= 1

        leftCount[val] += 1
        leftLen += 1

        # 리더 바꿔주기 -> 보통 같을 것이다.
        if leftCount[val] > leaderCount:
            leftLeader = val
            leaderCount = leftCount[val]

        # 과반수 체크하기 가장 많은 놈만 과반수로 설정됨.
        if leaderCount > leftLen / 2 and rightCount[leftLeader] > rightLen / 2:
            maxLeader += 1

    return maxLeader


A = [4, 3, 4, 4, 4, 2]
print(solution(A))
