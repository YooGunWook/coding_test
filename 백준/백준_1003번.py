val_list = []
t = int(input())
for _ in range(t):
    val_list.append(int(input()))


def fibonacci(n, memo):
    if n < 2:
        return n
    if memo[n] == 0:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


memo = [0] * 41
for i in val_list:
    if i == 0:
        print(1, 0)
    elif i == 1:
        print(0, 1)
    else:
        print(fibonacci(i - 1, memo), fibonacci(i, memo))
print(memo)