import collections
import ast
import sys

t = int(sys.stdin.readline())


def solution(command, arr):
    if command == "R":
        new_arr = collections.deque([])
        while arr:
            new_arr.append(arr.pop())
        return new_arr

    elif command == "D":
        arr.popleft()

    return arr


for _ in range(t):
    p = list(sys.stdin.readline())
    n = int(sys.stdin.readline())
    arr = ast.literal_eval(sys.stdin.readline())
    arr = collections.deque(arr)
    for command in p:
        if command == "D" and not arr:
            arr = "error"
            break
        else:
            arr = solution(command, arr)
    if arr == "error":
        print(arr)
    else:
        print(list(arr))
