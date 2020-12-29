"""
N으로 표현할 때 DP는 필수적이다.
i_index로 N으로 표현할 수 있는 값을 만들어준다. (5,55,555....)
그 후 DP 리스트 안에 있는 이전 사칙연산 결과를 대입해서 다시 한번 계산해준다.
만약 사칙연산 결과 값에 number가 있으면 해당 i_index 반환
"""


def solution(N, number):
    answer = -1
    DP = []
    for i_index in range(1, 9):
        number_set = {int(str(N) * i_index)}

        for j_index in range(0, i_index - 1):
            for x_value in DP[j_index]:
                for y_value in DP[-j_index - 1]:
                    number_set.add(x_value + y_value)
                    number_set.add(x_value - y_value)
                    number_set.add(y_value - x_value)
                    number_set.add(x_value * y_value)
                    if y_value != 0:
                        number_set.add(x_value // y_value)

        DP.append(number_set)
        if number in number_set:
            return i_index

    return answer
