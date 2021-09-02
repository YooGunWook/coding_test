"""
N개의 강의가 있다. 우리는 모든 강의의 시작하는 시간과 끝나는 시간을 알고 있다. 
이때, 우리는 최대한 적은 수의 강의실을 사용하여 모든 강의가 이루어지게 하고 싶다.
물론, 한 강의실에서는 동시에 2개 이상의 강의를 진행할 수 없고, 한 강의의 종료시간과 다른 강의의 시작시간이 겹치는 것은 상관없다. 
필요한 최소 강의실의 수를 출력하는 프로그램을 작성하시오.
"""
import heapq

n = int(input())
lessons = []
for _ in range(n):
    row = list(map(int, input().split(" ")))[1:] # 강의의 번호는 필요 없음
    lessons.append(row)

lessons = sorted(lessons, key=lambda x: x[0]) # 시작시간 기준 정렬

# 우선순위 큐로 해결
def solution(lessons):
    heap = [] # 강의실 담는 힙
    for lesson in lessons:
        if heap and heap[0] <= lesson[0]: # 수업이 더 늦게 시작하거나 끝나는 시간에 시작할 때 
            heapq.heappop(heap)
        heapq.heappush(heap, lesson[1]) # 새로운 강의 추가
    return len(heap)


print(solution(lessons))
