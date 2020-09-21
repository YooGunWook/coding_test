'''
내가 한 풀이 -> itertools를 쓰면 안좋다... ㅜㅜ
def solution(numbers):
    values = []
    for value in itertools.permutations(numbers):
        values.append(''.join([str(number) for number in value]))
    answer = str(max([int(value) for value in values]))
    return answer
'''


def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

