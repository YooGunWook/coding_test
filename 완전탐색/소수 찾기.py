import itertools


def number_check(numbers):
    number_list = []
    for index in range(1, len(numbers) + 1):
        number_list += [int(''.join(number)) for number in itertools.permutations(numbers, index)]
    return set(number_list)


def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if (number % i) == 0:
                break
            elif i == number -1:
                return True


def solution(numbers):
    number_list = number_check(numbers)
    count = 0
    for number in number_list:
        print(number)
        if is_prime(number):
            count += 1
    return count
