import time


def solution(nums: list) -> list:
    index_now = 0
    result = []
    while index_now != len(nums):
        product = 1
        for i_index in range(len(nums)):
            if index_now == i_index:
                continue
            product *= nums[i_index]
        index_now += 1
        result.append(product)
    return result


def book_solution(nums: list) -> list:
    out = []
    p = 1
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out


if __name__ == "__main__":
    now = time.time()
    print(solution([1, 2, 3, 4]), format(float(time.time() - now), "f"))
    now = time.time()
    print(book_solution([1, 2, 3, 4]), format(float(time.time() - now), "f"))

