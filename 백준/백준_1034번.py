import collections

# 데이터 구축
n, m = map(int, input().split(" "))
mat = []
for _ in range(n):
    row = list(input())
    mat.append(row)
k = int(input())


def solution(mat, k):
    max_on = 0  # 출력값
    for row in mat:  # 각 row별로 탐색
        row_count = collections.Counter(row)
        if row_count["0"] > k:  # k보다 0이 작으면 모든 램프를 켤 수 없기 때문에 continue
            continue
        # k보다 크고 둘의 나머지가 같아야 전부다 끌 수 있음
        if row_count["0"] <= k and k % 2 == row_count["0"] % 2:
            same_row = mat.count(row)  # 해당 행이랑 같은 애들의 개수를 세주면 최대 개수
            if same_row > max_on:
                max_on = same_row
    return max_on


print(solution(mat, k))
