from collections import deque


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    while progresses:
        count = 0
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        while True:
            if progresses[0] < 100:
                break
            else:
                progresses.popleft()
                speeds.popleft()
                count += 1
            if not progresses:
                break
        if count != 0:
            answer.append(count)

    return answer


if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    solution(progresses, speeds)
