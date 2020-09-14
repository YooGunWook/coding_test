priorities = [1, 1, 9, 1, 1, 1]
location = 0

def solution(priorities, location):

    maxValue = max(priorities)
    priorities_with_index = []
    answer = 0 


    for i in range(0, len(priorities)):
        priorities_with_index.append([i, priorities[i]])

    while priorities_with_index:
        front = priorities_with_index.pop(0)

        if any(front[1] < i[1] for i in priorities_with_index):
            priorities_with_index.append(front)
        else:
            answer += 1

            if front[0] == location:
                break
    

    return answer




print(solution(priorities,location))

