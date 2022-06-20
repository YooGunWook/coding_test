from itertools import permutations


def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    done_list = {}
    for i in range(len(numbers)):
        perms = set(int("".join(perm)) for perm in list(permutations(numbers, i + 1)))
        for perm in perms:
            if perm in done_list:
                continue
            if perm == 1 or perm == 0:
                continue
            if is_prime_number(perm):
                answer += 1
            done_list[perm] = 1
    return answer


if __name__ == "__main__":
    numbers = "011"
    print(solution(numbers))
