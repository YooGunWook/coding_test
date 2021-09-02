"""
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 
김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 
참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
수강신청 대충한 게 찔리면, 선생님을 도와드리자!
"""
import heapq
import collections

n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)

mat = sorted(mat, key=lambda x: x[0])  # 시작 시간을 기준으로 sorting

# 우선순위 큐 해결방식
def solution(mat):
    heap = []  # 강의실을 담을 힙
    for lesson in mat:  # 각 수업별로 탐색
        if heap and heap[0] <= lesson[0]:  # 가장 일찍 끝나는 시간 기준으로 탐색
            heapq.heappop(heap)
        heapq.heappush(heap, lesson[1])  # 새로운 강의 넣기
        # print(heap)
    return len(heap)


print(solution(mat))
