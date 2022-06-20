import sys

"""
그리디 서치 기반 풀이 
서류 성적 순으로 sorting
sorting 하고 나서 서류 1등은 무조건 통과이기 때문에 count는 1부터 시작
사람 한명씩 체크하면서 interview 순위가 현재보다 낮을 경우 interview 순위 갱신하고 count + 1해준다.
그러다가 인터뷰 1등이 나오면 종료.
"""


t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    score_list = []
    for j in range(n):
        s1, s2 = map(int, sys.stdin.readline().split(" "))
        score_list.append((s1, s2))
    score_list.sort(key=lambda x: x[0])
    count = 1
    interview = score_list[0][1]
    for person in score_list[1:]:
        if person[1] <= interview:
            count += 1
            interview = person[1]
        elif person[1] == 1:
            break
    print(count)
