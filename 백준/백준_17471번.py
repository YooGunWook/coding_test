import collections
from itertools import combinations

# 데이터 구축
n = int(input())
nums = list(map(int, input().split(" ")))
people_info = {}
graph = {}
for idx in range(n):
    people_info[idx + 1] = nums[idx]  # 각 노드별로 사람 수를 체크하는 용도로 만든다.

for _ in range(1, n + 1):
    graph[_] = list(map(int, input().split(" ")))[1:]  # 해당 node랑 연결된 다른 node 정보 저장

case = []
for i in range(1, n):  # 가질 수 있는 노드들 케이스를 만들어준다.
    cases = combinations(people_info.keys(), i)
    for comb in cases:
        case.append(comb)

# bfs를 통해 해당 노드들이 연결되어 있는지 확인
def bfs(graph, case_i, people_info):
    discovered = []
    val = 0
    i = case_i[0]  # 하나를 가지고 bfs로 탐색할 때 case_i와 동일한 결과가 나와야함
    queue = collections.deque([i])
    while queue:
        node = queue.popleft()
        if node not in discovered and node in case_i:
            discovered.append(node)
            for n_node in graph[node]:
                queue.append(n_node)
    if sorted(discovered) == sorted(case_i):  # 동일한 결과가 나오면 인구수를 구해준다.
        for dis in discovered:
            val += people_info[dis]
    return val


min_val = 10000000  # 동을 나눌 수 없는 케이스
for case_i in case:
    other_case = []  # 다른 후보의 노드들
    for i in range(1, n + 1):
        if i not in case_i:
            other_case.append(i)
    val = bfs(graph, case_i, people_info)  # 인구 수 계산
    other_val = bfs(graph, other_case, people_info)  # 다른 후보의 인구 수 계산
    if val == 0 or other_val == 0:  # 둘 중 하나라도 0이면 동을 나눌 수 없다는 의미
        continue
    min_val = min(min_val, abs(val - other_val))  # 최저 인구수를 구해준다.
if min_val == 10000000:  # 동을 나눌 수 없을 때
    print(-1)
else:  # 동이 나눠지고 최저일 때
    print(min_val)