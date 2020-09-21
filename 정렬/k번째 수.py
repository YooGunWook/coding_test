def solution(array, commands):
    answer = []
    for command in commands:
        new_array = sorted(array[command[0]-1: command[1]])
        value = new_array[command[2]-1]
        answer.append(value)
    return answer
