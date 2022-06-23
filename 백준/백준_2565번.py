from collections import defaultdict

"""
구현 기반 풀이
주의: 위 아래가 반대로 되어 있기 때문에 남쪽과 북쪽에 대해서 반대로 해줘야함.

"""

a, b = map(int, input().strip().split(" "))
n, m = map(int, input().strip().split(" "))

mat = []
for _ in range(b):
    row = [0] * a
    mat.append(row)

robot_info = defaultdict(list)
for i in range(n):
    robot = input().strip().split(" ")
    robot[0] = int(robot[0]) - 1
    robot[1] = int(robot[1]) - 1
    mat[robot[1]][robot[0]] = i + 1
    robot_info[i + 1].append(robot)

orders = []
for _ in range(m):
    o = input().split(" ")
    orders.append(o)


def order_robot(mat, orders, robot_info, a, b):
    direction = {"E": (1, 0), "N": (0, 1), "S": (0, -1), "W": (-1, 0)}
    for o in orders:
        r, od, c = o
        r = int(r)
        c = int(c)
        x, y, d = robot_info[r].pop()
        for _ in range(c):
            if od == "F":
                ox, oy = direction[d]
                nx, ny = x + ox, y + oy
                if 0 <= nx < a and 0 <= ny < b and mat[ny][nx] == 0:
                    mat[y][x] = 0
                    mat[ny][nx] = r
                    x = nx
                    y = ny
                elif 0 > nx or nx >= a or 0 > ny or ny >= b:
                    return f"Robot {r} crashes into the wall"
                elif mat[ny][nx] != 0:
                    return f"Robot {r} crashes into robot {mat[ny][nx]}"
            elif od == "R":
                if d == "E":
                    d = "S"
                elif d == "S":
                    d = "W"
                elif d == "W":
                    d = "N"
                else:
                    d = "E"
            elif od == "L":
                if d == "E":
                    d = "N"
                elif d == "N":
                    d = "W"
                elif d == "W":
                    d = "S"
                else:
                    d = "E"

        robot_info[r].append((x, y, d))
    return "OK"


print(order_robot(mat, orders, robot_info, a, b))

# 5 4
# 2 4
# 1 1 E
# 5 4 W
# 1 F 3
# 2 F 1
# 1 L 1
# 1 F 3

# 5 5
# 2 3
# 3 3 E
# 4 5 N
# 2 L 3
# 2 R 8
# 2 F 3
