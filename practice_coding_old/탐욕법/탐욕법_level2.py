def solution(people, limit):
    # 가벼운 사람부터 무거운 사람 순으로 sort 진행
    people.sort()
    
    # light한 사람과 무거운 사람을 비교하는 방식으로 진행. 
    # 그러다가 둘이 더해서 100 이하가 되면 light에 1 더해주고 heavy는 1 빼주고, count에 1 더해주는 방식으로 진행
    # else 문으로는 heavy만 빼준다.
    # 이걸 계속 반복하다가 light가 heavy보다 커지는 경우 break
    # 어차피 탈 수 있는 사람은 최대 2명이고 limit 제한이 있기 때문에
    # 사람수에서 2명만 탄 경우를 빼주면 구명보트가 몇개 필요한 지 나오게 된다. 
    length = len(people)
    light = 0
    heavy = length - 1
    count = 0
    while (light < heavy):
        if people[light] + people[heavy] <= limit:
            light += 1
            heavy -= 1
            count += 1
        else:
            heavy -= 1
    answer = length - count
    return answer