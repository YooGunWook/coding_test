"""
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
"""
import collections

n, k = list(map(int, input().split(" ")))
time_chk = collections.defaultdict(int)  # 시간체크용
time_chk[n] = 0  # 시작하는 부분은 0초부터 시작


def bfs(n, k):  # bfs 기반으로 해결
    queue = collections.deque([n])
    while queue:
        p = queue.popleft()
        x1 = p + 1
        x2 = p - 1
        t_m = time_chk[p] + 1
        x3 = 2 * p
        fin_1 = 10000000000
        fin_2 = 10000000000

        # 정답 체크할 때 사용
        if x1 == k or x2 == k:
            fin_1 = t_m
        if x3 == k or p == k:
            fin_2 = time_chk[p]

        # 둘 중 더 작은 부분에서 정답 처리
        if fin_1 != 10000000000 or fin_2 != 10000000000:
            return min(fin_1, fin_2)

        # 2를 곱하는 케이스
        if (x3 not in time_chk or time_chk[x3] > time_chk[p]) and 0 <= x3 <= 100000:
            time_chk[x3] = time_chk[p]
            queue.append(x3)

        # 1을 빼주는 케이스
        if (x2 not in time_chk or time_chk[x2] > t_m) and 0 <= x2 <= 100000:
            time_chk[x2] = t_m
            queue.append(x2)

        # 1을 더해주는 케이스
        if (x1 not in time_chk or time_chk[x1] > t_m) and 0 <= x1 <= 100000:
            time_chk[x1] = t_m
            queue.append(x1)


print(bfs(n, k))

