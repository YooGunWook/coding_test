# 링크드리스트 풀이 (dict 기반)
def solution(n, k, cmds):
    ans = ""  # 정답
    stack = []  # 지워진 node에 대한 정보

    # chart 만들어 주기
    chart = {0: [n - 1, 1]}  # [이전 노드, 다음 노드]
    for i in range(1, n):
        if i == n - 1:
            chart[i] = [i - 1, 0]
        else:
            chart[i] = [i - 1, i + 1]

    for cmd in cmds:  # 각 명령어 체크
        if len(cmd) > 1:  # 1 보다 크면 위 아래 옮기기
            c, x = cmd.split(" ")
            cnt = 0
            if c == "D":  # 내려가는 케이스
                while cnt < int(x):
                    k = chart[k][1]
                    cnt += 1
            else:  # 올라가는 케이스
                while cnt < int(x):
                    k = chart[k][0]
                    cnt += 1

        elif cmd == "C":  # 지우기
            chart[chart[k][0]][1] = chart[k][1]  # 이전 노드의 다음 노드 변경
            chart[chart[k][1]][0] = chart[k][0]  # 다음 노드의 이전 노드 변경
            stack.append([k, chart[k]])  # 지운 정보 저장
            tmp = chart[k]  # 노드 체크용
            del chart[k]

            # 가장 마지막인지 아닌지 체크
            if tmp[1] == 0:
                k = tmp[0]
            else:
                k = tmp[1]

        else:  # 다시 채우기
            row, row_list = stack.pop()
            row_0, row_1 = row_list
            chart[row] = [row_0, row_1]
            chart[row_0][1] = row  # 이전 노드에 채우는 값 넣기
            chart[row_1][0] = row  # 다음 노드에 채우는 값 넣기

    for i in range(n):
        if i not in chart:
            ans += "X"
            continue
        ans += "O"
    return ans


cmds = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(8, 2, cmds))


def solution(n, k, cmds):
    ans = ""
    stack = []
    chart = {0: [n - 1, 1]}
    for i in range(1, n):
        if i == n - 1:
            chart[i] = [i - 1, 0]
            continue
        chart[i] = [i - 1, i + 1]

    for cmd in cmds:
        if len(cmd) > 1:
            c, x = cmd.split(" ")
            if c == "D":
                for _ in range(int(x)):
                    k = chart[k][1]
            else:
                for _ in range(int(x)):
                    k = chart[k][0]
        elif cmd == "C":
            chart[chart[k][0]][1] = chart[k][1]
            chart[chart[k][1]][0] = chart[k][0]
            stack.append([k, chart[k]])
            tmp = chart[k]
            del chart[k]

            if tmp[1] == 0:
                k = tmp[0]
            else:
                k = tmp[1]

        elif cmd == "Z":
            row, row_list = stack.pop()
            pre, nex = row_list
            chart[row] = [pre, nex]
            chart[pre][1] = row
            chart[nex][0] = row

    for i in range(n):
        if i not in chart:
            ans += "X"
            continue
        ans += "O"
    return ans


cmds = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(8, 2, cmds))
