"""
0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.
덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 
또한 한 개의 수를 여러 번 쓸 수도 있다.
"""

n, k = list(map(int, input().split(" ")))


def solution(n, k):
    table = [1]
    table += [0] * n
    # DP 기반 풀이
    # table(n, k) = table(n, k-1) + table(n-1, k)
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            table[j] = (table[j] + table[j - 1]) % 1000000000
    return table


print(solution(n, k)[k])
