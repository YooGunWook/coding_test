from collections import deque


def solution(people, limit):
    """
    deque를 활용한 풀이
    처음과 끝 값을 더했을 때 limit보다 작을 경우 둘을 빼고,
    limit보다 클 경우 처음만 popleft를 한다.
    answer는 1씩 더해준다.
    """
    answer = 0
    people = deque(sorted(people, reverse=True))
    while people:
        if len(people) == 1:
            answer += 1
            break
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else:
            people.popleft()
        answer += 1

    return answer


if __name__ == "__main__":
    people = [70, 50, 80, 50]
    limit = 100
    print(solution(people, limit))
