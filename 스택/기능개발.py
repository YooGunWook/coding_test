import collections


def solution(progresses, speeds):
    queue = collections.deque()
    for progress, speed in zip(progresses, speeds):
        count = 0
        while progress < 100:
            if progress >= 100:
                break
            progress += speed
            count += 1
        queue.append(count)

    for qu in range(1, len(queue)):
        if queue[qu] <= queue[qu - 1]:
            queue[qu] = queue[qu - 1]

    return list(collections.Counter(queue).values())