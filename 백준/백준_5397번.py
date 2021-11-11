n = int(input())


def solution(n):
    for _ in range(n):
        password = list(input().strip())
        # solve problem by two stacks
        str1 = []
        str2 = []
        for code in password:
            if code == "<":
                if not str1:  # 예외처리
                    continue
                str2.append(str1.pop())

            elif code == ">":
                if not str2:  # 예외처리
                    continue
                str1.append(str2.pop())

            elif code == "-":
                if not str1:  # 지울게 없을때
                    continue
                str1.pop()

            else:
                str1.append(code)
        print("".join(str1 + str2[::-1]))


solution(n)
