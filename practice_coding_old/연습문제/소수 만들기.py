import itertools

# 소수 판별 함수
# 2보다 작으면 무조건 False
# 2나 3이면 소수다.
# 2 또는 3으로 나눠지면 소수가 아니다.
# 10 미만의 값들은 2나 3으로만 나눠지지 않으면 된다. 
# 그 이상의 수들에 대해서는 5, 7, 9, 11, 13, 15... 등의 홀수로 나눠보면 된다. 하지만 이미 3의 배수에 대해서는 앞에서 검사하기 때문에 5, 7, 11, 15,... 의 패턴으로 검사할 수 있다.
# N이 소수인지를 알고 싶으면 N의 제곱근까지만 검사해보면 된다.

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True
    k, l = 5, n ** 0.5
    
    while k <= l:
        if n % k == 0 or n % (k+2) == 0:
            return False 
        k += 6
    return True


def solution(nums):
    answer = 0
    nums = list(itertools.combinations(nums,3))
    for i in nums:
        n = sum(i)
        if is_prime(n):
            answer += 1

    return answer