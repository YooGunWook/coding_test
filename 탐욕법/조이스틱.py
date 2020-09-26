import string


'''
우선 위 아래는 간단하기 때문에 이 과정을 먼저 함수로 구현
그 다음 양옆으로 가는 것을 구현해야되는데, A의 여부에 따라 판단하면 좋을 듯 하다
'''


def count_alpha(alpha):
    up = 0
    down = 0
    alpha_list = list(string.ascii_uppercase)[1:]
    alpha_list_reverse = alpha_list[::-1]

    if alpha == 'A':
        return up

    for alpha_up in alpha_list:
        if alpha != alpha_up:
            up += 1

        if alpha == alpha_up:
            up += 1
            break

    for alpha_down in alpha_list_reverse:
        if alpha != alpha_down:
            down += 1

        if alpha == alpha_down:
            down += 1
            break

    if up == down:
        return up

    if up > down:
        return down

    if up < down:
        return up


def solution(name):
    count = [count_alpha(i) for i in name]
    answer = 0
    where = 0
    while True:
        answer += count[where]
        print(answer)
        count[where] = 0
        print(count)

        if sum(count) == 0:
            break

        left = 1
        right = 1

        while count[where - left] <= 0:
            left += 1
        while count[where + right] <= 0:
            right += 1

        answer += left if left < right else right
        where += -left if left < right else right

    return answer

