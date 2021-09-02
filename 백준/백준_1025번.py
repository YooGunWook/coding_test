n = int(input())
cube = list(map(int, input().split(" ")))


def solution(n, cube):
    sum_value = 0  # 출력값
    sum_list = []  # 더해야될 번호들
    if n == 1:  # 하나일 때는 한면만 안보이면 됨
        return sum(sorted(cube)[0:5])

    # 0,5 1,4 2,3 에서 작은 값들만 구한다.
    sum_list.append(min(cube[0], cube[5]))
    sum_list.append(min(cube[1], cube[4]))
    sum_list.append(min(cube[2], cube[3]))
    sum_list = sorted(sum_list)

    # 1,2,3면만 보이게 되는데, 그때 나오는 값들
    min1 = sum_list[0]
    min2 = sum_list[0] + sum_list[1]
    min3 = sum_list[0] + sum_list[1] + sum_list[2]

    # 각 면이 보이는 수
    n1 = (n - 2) * (n - 2) + 4 * (n - 1) * (n - 2)
    n2 = 4 * (n - 2) + 4 * (n - 1)
    n3 = 4

    # 모두 더하기
    sum_value += n1 * min1
    sum_value += n2 * min2
    sum_value += n3 * min3

    return sum_value


print(solution(n, cube))