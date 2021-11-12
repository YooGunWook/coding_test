n = int(input())


def solution(n):
    word_list = []  # 타이핑 될 단어를 넣어줄 리스트
    word = ""  # 타이핑된 단어
    for _ in range(n):
        cmd = input().strip().split(" ")
        # 명령어 단위로 단어를 넣어준다.
        if cmd[0] == "type":
            word += cmd[1]
            word_list.append([word, int(cmd[2])])
        # undo를 할 때 t2 - t1 시점의 이전 단어를 선택하게 한다.
        # 만약 없으면 ""가 들어가게 된다.
        elif cmd[0] == "undo":
            t1 = int(cmd[1])
            t2 = int(cmd[2])
            t3 = t2 - t1
            word = ""
            # 반대로 탐색
            for i in range(len(word_list) - 1, -1, -1):
                if word_list[i][1] < t3:
                    word = word_list[i][0]
                    break
            word_list.append([word, t2])

    return word_list[-1][0]


print(solution(n))
