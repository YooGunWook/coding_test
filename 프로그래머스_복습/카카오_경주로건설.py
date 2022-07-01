import heapq
from collections import defaultdict


def solution(board):
    """
    우선순위 힙으로 구현
    함정: 중간에 겹치는 부분이 생길 수 있는데 무조건 크다고 넘기지 말고 방향에 따른 값을 따로 저장해줘야함.
    dict에다가 right, left, down, up에 대해서 값을 보여줘야함.
    """
    queue = [[0, 0, 0, "dir", False]]
    heapq.heapify(queue)
    dir_list = {"right": (0, 1), "left": (0, -1), "down": (1, 0), "up": (-1, 0)}
    n = len(board)
    visited = [[0] * n for _ in range(n)]
    visited_dict = defaultdict(dict)
    answer = 1e9
    while queue:
        cost, x, y, d, flag = heapq.heappop(queue)
        if x == n - 1 and y == n - 1:
            answer = min(answer, cost)
            continue
        for nd in dir_list:
            nx = x + dir_list[nd][0]
            ny = y + dir_list[nd][1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                if cost == 0:
                    heapq.heappush(queue, [100, nx, ny, nd, False])
                    visited[nx][ny] = 1
                    visited_dict[(nx, ny)][nd] = 100
                else:
                    if (
                        (d == "right" and nd == "left")
                        or (d == "left" and nd == "right")
                        or (d == "up" and nd == "down")
                        or (d == "down" and nd == "up")
                    ):
                        continue
                    elif (
                        (d == "right" or d == "left")
                        and (nd == "up" or nd == "down")
                        and not flag
                    ):
                        heapq.heappush(queue, [cost + 500, x, y, nd, True])
                    elif (
                        (d == "up" or d == "down")
                        and (nd == "left" or nd == "right")
                        and not flag
                    ):
                        heapq.heappush(queue, [cost + 500, x, y, nd, True])
                    elif (nd == d and nd not in visited_dict[(nx, ny)]) or (
                        nd == d and visited_dict[(nx, ny)][nd] >= cost + 100
                    ):
                        heapq.heappush(queue, [cost + 100, nx, ny, nd, False])
                        visited[nx][ny] = 1
                        visited_dict[(nx, ny)][nd] = cost + 100

    return answer


if __name__ == "__main__":
    mat = []
    for _ in range(8):
        row = list(map(int, list(input())))
        mat.append(row)
    print(solution(mat))
