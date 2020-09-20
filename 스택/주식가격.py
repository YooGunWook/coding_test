import collections


def solution(prices):
    queue = collections.deque()
    for price in range(0, len(prices) - 1):
        count = 0
        for price_check in range(price + 1, len(prices)):
            if prices[price] <= prices[price_check]:
                count += 1
            elif prices[price] > prices[price_check]:
                count += 1
                break
        queue.append(count)
    queue.append(0)
    answer = list(queue)
    return answer


