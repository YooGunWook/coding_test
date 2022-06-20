def solution(price, money, count):
    total_money = 0
    for i in range(1, count + 1):
        total_money += price * i
    if money >= total_money:
        return 0
    return total_money - money