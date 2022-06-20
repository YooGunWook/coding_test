from collections import deque


def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    pri_idx = deque([i for i in range(len(priorities))])
    printed = 0
    max_pri = max(priorities)
    while priorities:
        target = priorities.popleft()
        idx = pri_idx.popleft()
        if target < max_pri:
            priorities.append(target)
            pri_idx.append(idx)
        else:
            printed += 1
            max_pri = max(priorities)

            if idx == location:
                answer = printed
                break
    return answer


if __name__ == "__main__":
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    solution(priorities, location)
