import sys

""" 
이분 탐색 기반 풀이
시작 지점이 end보다 작거나 같아질 때 까지 진행
시작을 1, 끝을 끝 - 시작으로 진행.
둘 간의 거리를 최대로 하기 위해서는 middle보다 커야한다. 
x를 갱신해서 공유기 위치를 조정한다. 
cnt가 c보다 크거나 같을 경우 -> 공유기를 많이 설치한 케이스 -> start 업데이트 하고, ans를 middle로 설정 
cnt가 c보다 적을 경우 -> 공유기를 적게 설치한 케이스 -> end 업데이트 
"""

n, c = map(int, sys.stdin.readline().split(" "))
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()

start = 1
end = house[-1] - house[0]

while start <= end:
    middle = (start + end) // 2
    x = house[0]
    cnt = 1
    
    for i in range(len(house)):
        if house[i] - x >= middle:
            x = house[i]
            cnt += 1
    
    if cnt >= c:
        start = middle + 1
        ans = middle
    elif cnt < c:
        end = middle - 1

print(ans)
        