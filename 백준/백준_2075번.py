"""
N×N의 표에 수 N2개 채워져 있다. 채워진 수에는 한 가지 특징이 있는데, 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것이다. N=5일 때의 예를 보자.

12	7	9	15	5
13	8	11	19	6
21	10	26	31	16
48	14	28	35	25
52	20	32	41	49
이러한 표가 주어졌을 때, N번째 큰 수를 찾는 프로그램을 작성하시오. 표에 채워진 수는 모두 다르다.
"""
import heapq

n = int(input())
# mat = []
# for _ in range(n):
#     row = list(map(int, input().split(" ")))
#     mat.append(row)

# 우선순위 큐 기반 
def solution(n):
    '''
    최소 힙으로 구현
    '''
    heap = [] # 힙 리스트
    for _ in range(n): 
        row = list(map(int, input().split(" ")))
        if not heap: # 힙이 없을 때는 바로 넣어준다.
            for val in row:
                heapq.heappush(heap, val)
        else: # 그외
            for val in row:
                if heap[0] < val: # 0번째가 결국 우리가 원하는 값임. 
                    # n번째로 큰 수 
                    heapq.heappush(heap, val) # 큰 값 넣어주기
                    heapq.heappop(heap) # 빼주기

    return heap[0]


print(solution(n))
