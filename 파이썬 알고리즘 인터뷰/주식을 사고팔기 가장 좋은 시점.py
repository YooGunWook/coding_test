import sys
import time


def solution(nums: list) -> int:
    profit = 0
    min_value = sys.maxsize
    for price in nums:
        min_value = min(min_value, price)
        profit = max(profit, price - min_value)
    return profit


if __name__ == "__main__":
    now = time.time()
    print(solution([7, 1, 5, 3, 6, 4]), format(float(time.time() - now), "f"))

