def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[0])
    end = routes[0][1]
    for car in routes:
        if end < car[0]:
            answer += 1
            end = car[1]
        if end >= car[1]:
            end = car[1]
    return answer
