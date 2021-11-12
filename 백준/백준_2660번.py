"""
월드컵 축구의 응원을 위한 모임에서 회장을 선출하려고 한다. 
이 모임은 만들어진지 얼마 되지 않았기 때문에 회원 사이에 서로 모르는 사람도 있지만, 몇 사람을 통하면 모두가 서로 알 수 있다. 
각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다.

예를 들어 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다. 
어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의 친구임을 말한다. 
또한 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친구의 친구의 친구임을 말한다.

4점, 5점 등은 같은 방법으로 정해진다. 
각 회원의 점수를 정할 때 주의할 점은 어떤 두 회원이 친구사이이면서 동시에 친구의 친구사이이면, 이 두사람은 친구사이라고 본다.

회장은 회원들 중에서 점수가 가장 작은 사람이 된다. 
회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램을 작성하시오.
"""
import collections

n = int(input())
graph = {i + 1: [] for i in range(n)}
while True:
    a, b = list(map(int, input().split(" ")))
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

# bfs 기반 풀이
def solution(graph, node):
    visited = [node]  # 방문한 노드 확인
    queue = collections.deque([[node, 0]])
    max_dist = -1e9  # 가장 긴 길이를 찾아야함
    while queue:
        n, dist = queue.popleft()
        for n_node in graph[n]:
            if n_node not in visited:
                visited.append(n_node)
                queue.append([n_node, dist + 1])
                if dist + 1 > max_dist:  # 최대 길이 업데이트
                    max_dist = dist + 1
    return max_dist


score_dict = collections.defaultdict(list)  # 점수별 사람들 정보
min_score = 1e9
for i in graph:  # 각 노드별로 탐색 진행
    score = solution(graph, i)
    if score == 0:
        continue
    if score < min_score:  # 최소 점수 업데이트
        min_score = score
    score_dict[score].append(i)
print(f"{min_score} {len(score_dict[min_score])}")
print(*sorted(score_dict[min_score]))