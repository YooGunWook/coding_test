import collections
import ast
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline()
    # p = p.replace("RR", "R")
    n = int(sys.stdin.readline())
    arr = collections.deque([str(i) for i in ast.literal_eval(sys.stdin.readline())])
    order = "nr"
    error_code = False
    for o in p:
        if o == "R":
            if order == "nr":
                order = "r"
            else:
                order = "nr"
        elif o == "D":
            if not arr:
                error_code = True
                break
            if order == "nr":
                arr.popleft()
            elif order == "r":
                arr.pop()
                
    if error_code:
        print("error")
        continue 
    if order == "nr":
        print("[" + ",".join(list(arr)) + "]")
    elif order == "r":
        print("[" + ",".join(list(arr)[::-1]) + "]")
                
                
        