import collections

# 자료 구축
n = int(input())
k = int(input())
mat = []
for _ in range(n):
    row = [0] * n
    mat.append(row)
for _ in range(k):
    x, y = list(map(int, input().split(" ")))
    mat[x - 1][y - 1] = 1

l = int(input())
rotate_info = collections.deque([])
for _ in range(l):
    x, c = input().split(" ")
    rotate_info.append((int(x), c))

snake = collections.deque([(0, 0)])


def game(mat, rotate_info, snake):  # 지렁이 게임 시작
    direction = 1  # 방향
    time = 0
    while True:
        x, y = snake.pop()

        if direction == 1:  # 오른쪽을 볼 때
            if (x, y + 1) in snake or y + 1 >= n:  # 이 조건은 머리가 몸에 닿거나 벽에 닿을 때
                time += 1
                break

            if mat[x][y + 1] == 1:
                snake.append((x, y))
                snake.append((x, y + 1))
                mat[x][y + 1] = 0
                time += 1
            else:
                if not snake:
                    snake.append((x, y + 1))
                    time += 1
                else:
                    snake.popleft()
                    snake.append((x, y))
                    snake.append((x, y + 1))
                    time += 1

        elif direction == 2:  # 아래를 볼 때
            if (x + 1, y) in snake or x + 1 >= n:  # 이 조건은 머리가 몸에 닿거나 벽에 닿을 때
                time += 1
                break

            if mat[x + 1][y] == 1:
                snake.append((x, y))
                snake.append((x + 1, y))
                mat[x + 1][y] = 0
                time += 1
            else:
                if not snake:
                    snake.append((x + 1, y))
                    time += 1
                else:
                    snake.popleft()
                    snake.append((x, y))
                    snake.append((x + 1, y))
                    time += 1

        elif direction == 3:  # 왼쪽을 볼 때
            if (x, y - 1) in snake or 0 > y - 1:  # 이 조건은 머리가 몸에 닿거나 벽에 닿을 때
                time += 1
                break
            if mat[x][y - 1] == 1:
                snake.append((x, y))
                snake.append((x, y - 1))
                mat[x][y - 1] = 0
                time += 1
            else:
                if not snake:
                    snake.append((x, y - 1))
                    time += 1
                else:
                    snake.popleft()
                    snake.append((x, y))
                    snake.append((x, y - 1))
                    time += 1

        elif direction == 4:  # 위를 볼 때
            if (x - 1, y) in snake or 0 > x - 1:  # 이 조건은 머리가 몸에 닿거나 벽에 닿을 때
                time += 1
                break
            if mat[x - 1][y] == 1:
                snake.append((x, y))
                snake.append((x - 1, y))
                mat[x - 1][y] = 0
                time += 1
            else:
                if not snake:
                    snake.append((x - 1, y))
                    time += 1
                else:
                    snake.popleft()
                    snake.append((x, y))
                    snake.append((x - 1, y))
                    time += 1
        if not rotate_info:
            continue
        if time == rotate_info[0][0]:  # 머리가 회전할 때
            ro_time, ro_dir = rotate_info.popleft()
            if ro_dir == "D":  # 오른쪽
                if direction == 4:
                    direction = 1
                else:
                    direction += 1

            elif ro_dir == "L":  # 왼쪽
                if direction == 1:
                    direction = 4
                else:
                    direction -= 1
    return time


print(game(mat, rotate_info, snake))
