import collections


def solution(priorities, location):
    priorities_with_index = collections.deque()
    answer = 0

    for index in range(0, len(priorities)):
        priorities_with_index.append([index, priorities[index]])

    while priorities_with_index:
        front = priorities_with_index.popleft()
        if any(front[1] < value[1] for value in priorities_with_index):
            priorities_with_index.append(front)
        else:
            answer += 1

            if front[0] == location:
                break

    return answer
