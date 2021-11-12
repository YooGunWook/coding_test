import sys

string = sys.stdin.readline().strip()
n = len(string)
m = int(sys.stdin.readline())


def solution(string, m):
    # stack 두개로 문제 해결
    str1 = list(string)
    str2 = []

    for _ in range(m):
        cmd = sys.stdin.readline().strip()
        if cmd[0] == "L" and str1:
            str2.append(str1.pop())
        elif cmd[0] == "D" and str2:
            str1.append(str2.pop())
        elif cmd[0] == "B" and str1:  # 왼쪽 제거
            str1.pop()
        elif cmd[0] == "P":  # 왼쪽에 추가
            str1.append(cmd[-1])

    str2 = str2[::-1]  # 스택이기 때문에 reverse해준다.

    return "".join(str1 + str2)


print(solution(string, m))

