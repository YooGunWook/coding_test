import itertools

# 자료 구축
n, m = list(map(int, input().split(" ")))
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)

chicken_house = []  # 현재 치킨집 좌표
house = []  # 현재 있는 집 좌표
for i in range(n):
    for j in range(n):
        if mat[i][j] == 2:
            chicken_house.append((i + 1, j + 1))
        if mat[i][j] == 1:
            house.append((i + 1, j + 1))


min_chi_dis = 10000000000  # 도시의 치킨 최소 거리
chicken_cases = itertools.combinations(chicken_house, m)  # 조합을 활용해서 최적의 도시 치킨 거리를 구한다.
for chicken_case in chicken_cases:  # 각 케이스별로 검사
    sum_dist = 0  # 각 케이스별 최소 치킨 거리
    for ho in house:  # 각 집별로 치킨 거리 구하기
        min_dist = 10000000
        for chicken in chicken_case:
            dist = abs(chicken[0] - ho[0]) + abs(chicken[1] - ho[1])
            if min_dist > dist:
                min_dist = dist
        sum_dist += min_dist
    if min_chi_dis > sum_dist:
        min_chi_dis = sum_dist

print(min_chi_dis)