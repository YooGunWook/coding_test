from collections import deque

n, k = map(int, input().split())

# bfs 기반 풀이
def solution(n, k):
    visited = [100000] * 100001 # 방문 목록 확인 및 시간 체크
    queue = deque([[n, 0]]) 
    min_time = 1e9 # 최소 시간
    case_count = 0 # 몇가지 루트가 있는지 체크

    while queue:
        now, time = queue.popleft()
        if now == k and min_time >= time:
            if min_time != time: # 혹시라도 더 짧은 시간이 있을 때 
                min_time = time
                case_count = 1
            else: # 그 외 
                case_count += 1
            continue

        # 각 케이스별로 만들어주기
        plus_1 = now + 1
        minus_1 = now - 1
        multi_2 = now * 2
        cases = [plus_1, minus_1, multi_2]
        new_time = time + 1

        # 각 케이스에 대해서 검사
        for case in cases:
            if 0 <= case <= 100000 and visited[case] >= new_time:
                visited[case] = new_time
                queue.append([case, new_time])

    return min_time, case_count


fin_time, fin_case = solution(n, k)
print(fin_time)
print(fin_case)
