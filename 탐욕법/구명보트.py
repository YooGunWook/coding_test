import collections


def solution(people, limit):
    people = sorted(people)
    people = collections.deque(people)
    count = 0

    while people:
        if len(people) == 1:
            count += 1
            break

        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            count += 1
        else:
            people.pop()
            count += 1

    return count
