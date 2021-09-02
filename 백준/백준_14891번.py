import collections
import sys

first = collections.deque(list(sys.stdin.readline())[:8])
second = collections.deque(list(sys.stdin.readline())[:8])
third = collections.deque(list(sys.stdin.readline())[:8])
forth = collections.deque(list(sys.stdin.readline())[:8])

# first = collections.deque(list("10010011"))
# second = collections.deque(list("01010011"))
# third = collections.deque(list("11100011"))
# forth = collections.deque(list("01010101"))

count = int(sys.stdin.readline().strip())

for _ in range(count):
    target, direction = map(int, sys.stdin.readline().split())
    if direction == -1:
        four_flag = False
        three_flag = False
        two_flag = False
        one_flag = False

        if target == 1:
            if first[2] != second[6]:
                two_flag = True
                one_flag = True
                if second[2] != third[6]:
                    three_flag = True
                    if third[2] != forth[6]:
                        four_flag = True

            tmp = first.popleft()
            first.append(tmp)
            if two_flag == True:
                tmp = second.pop()
                second.appendleft(tmp)
            if three_flag == True:
                tmp = third.popleft()
                third.append(tmp)
            if four_flag == True:
                tmp = forth.pop()
                forth.appendleft(tmp)

        elif target == 2:
            if second[2] != third[6]:
                two_flag = True
                three_flag = True
                if third[2] != forth[6]:
                    four_flag = True
            if second[6] != first[2]:
                one_flag = True
                two_flag = True

            if one_flag == True:
                tmp = first.pop()
                first.appendleft(tmp)
            tmp = second.popleft()
            second.append(tmp)
            if three_flag == True:
                tmp = third.pop()
                third.appendleft(tmp)
            if four_flag == True:
                tmp = forth.popleft()
                forth.append(tmp)

        elif target == 3:
            if third[2] != forth[6]:
                four_flag = True
                three_flag = True
            if third[6] != second[2]:
                two_flag = True
                three_flag = True
                if second[6] != first[2]:
                    one_flag = True

            tmp = third.popleft()
            third.append(tmp)
            if four_flag == True:
                tmp = forth.pop()
                forth.appendleft(tmp)
            if two_flag == True:
                tmp = second.pop()
                second.appendleft(tmp)
            if one_flag == True:
                tmp = first.popleft()
                first.append(tmp)

        elif target == 4:
            if forth[6] != third[2]:
                four_flag = True
                three_flag = True
                if third[6] != second[2]:
                    two_flag = True
                    if second[6] != first[2]:
                        one_flag = True

            if one_flag == True:
                tmp = first.pop()
                first.appendleft(tmp)
            if two_flag == True:
                tmp = second.popleft()
                second.append(tmp)
            if three_flag == True:
                tmp = third.pop()
                third.appendleft(tmp)
            tmp = forth.popleft()
            forth.append(tmp)

    if direction == 1:
        four_flag = False
        three_flag = False
        two_flag = False
        one_flag = False

        if target == 1:
            if first[2] != second[6]:
                two_flag = True
                one_flag = True
                if second[2] != third[6]:
                    three_flag = True
                    if third[2] != forth[6]:
                        four_flag = True

            tmp = first.pop()
            first.appendleft(tmp)
            if two_flag == True:
                tmp = second.popleft()
                second.append(tmp)
            if three_flag == True:
                tmp = third.pop()
                third.appendleft(tmp)
            if four_flag == True:
                tmp = forth.popleft()
                forth.append(tmp)

        elif target == 2:
            if second[2] != third[6]:
                two_flag = True
                three_flag = True
                if third[2] != forth[6]:
                    four_flag = True
            if second[6] != first[2]:
                one_flag = True
                two_flag = True

            if one_flag == True:
                tmp = first.popleft()
                first.append(tmp)
            tmp = second.pop()
            second.appendleft(tmp)
            if three_flag == True:
                tmp = third.popleft()
                third.append(tmp)
            if four_flag == True:
                tmp = forth.pop()
                forth.appendleft(tmp)

        elif target == 3:
            if third[2] != forth[6]:
                four_flag = True
                three_flag = True
            if third[6] != second[2]:
                two_flag = True
                three_flag = True
                if second[6] != first[2]:
                    one_flag = True

            tmp = third.pop()
            third.appendleft(tmp)
            if four_flag == True:
                tmp = forth.popleft()
                forth.append(tmp)
            if two_flag == True:
                tmp = second.popleft()
                second.append(tmp)
            if one_flag == True:
                tmp = first.pop()
                first.appendleft(tmp)

        elif target == 4:
            if forth[6] != third[2]:
                four_flag = True
                three_flag = True
                if third[6] != second[2]:
                    two_flag = True
                    if second[6] != first[2]:
                        one_flag = True

            if one_flag == True:
                tmp = first.popleft()
                first.append(tmp)
            if two_flag == True:
                tmp = second.pop()
                second.appendleft(tmp)
            if three_flag == True:
                tmp = third.popleft()
                third.append(tmp)
            tmp = forth.pop()
            forth.appendleft(tmp)
    print(first)
    print(second)
    print(third)
    print(forth)


score = 0
if first[0] == "1":
    score += 1
if second[0] == "1":
    score += 2
if third[0] == "1":
    score += 4
if forth[0] == "1":
    score += 8

print(score)
