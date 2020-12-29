def summation(num: list, target: int) -> list:
    result = []
    for i_index in range(0, len(num) - 1):
        for j_index in range(1, len(num)):
            if num[i_index] + num[j_index] == target:
                result.append(i_index)
                result.append(j_index)
                break
    return result


# 다른 풀이


def summation_fix(num: list, target: int) -> list:
    for i_index, number in enumerate(num):
        check_number = target - number
        if check_number in num[i_index + 1 :]:
            return [
                num.index(number),
                num[i_index + 1 :].index(check_number) + (i_index + 1),
            ]


# 다른 풀이


def summation_new(num: list, target: int) -> list:
    nums_map = {}
    for i_index, number in enumerate(num):
        nums_map[number] = i_index

    for i_index, number in enumerate(num):
        if target - number in nums_map and i_index != nums_map[target - number]:
            return [i_index, nums_map[target - number]]


# 조회 구조 개선 모델


def summation_new_fix(num: list, target: int) -> list:
    nums_map = {}
    for i_index, number in enumerate(num):
        if target - number in nums_map:
            return [nums_map[target - number], i_index]
        nums_map[number] = i_index


# 투 포인터 활용 -> 원래는 사용할 수 없지만 이 문제는 정렬 되어 있기 때문에 가능
# 나중에 이걸 활용할때는 정렬을 하자


def two_pointer(num: list, target: int) -> list:
    left, right = 0, len(num) - 1
    while left != right:
        if num[left] + num[right] > target:
            right -= 1
        elif num[left] + num[right] < target:
            left += 1
        elif num[left] + num[right] == target:
            return [left, right]


if __name__ == "__main__":
    print(two_pointer([2, 7, 11, 15], 9))

