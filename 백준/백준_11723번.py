import sys

n = int(sys.stdin.readline())
S = 0b0
all_S = 0b111111111111111111111
not_S = 0b000000000000000000000


def solution(S, val, h):
    if h == "add":
        S = S | (1 << val)
    elif h == "remove":
        S = S & ~(1 << val)
    elif h == "check":
        if S & (1 << val):
            print(1)
        else:
            print(0)
    elif h == "toggle":
        S = S ^ (1 << val)
    elif h == "all":
        S = S | all_S
    else:
        S = S & not_S
    return S


for _ in range(n):
    cmd = sys.stdin.readline().rstrip()
    if "all" in cmd or "empty" in cmd:
        h = cmd
        val = 0
    else:
        h, val = cmd.split(" ")
        val = int(val)
    S = solution(S, val, h)
