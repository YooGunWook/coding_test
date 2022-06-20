from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        count = 0
        price = prices.popleft()
        if prices:
            for tmp in prices:
                if price <= tmp:
                    count += 1
                else:
                    count += 1
                    break
            answer.append(count)
        else:
            answer.append(count)

    return answer


if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))
