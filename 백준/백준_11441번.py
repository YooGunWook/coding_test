import collections

N = 5
N_list = [1, 0, -1]
cum = [N_list[0]]
for value in N_list[1:]:
    cum.append(cum[-1] + value)
M = 5


def solution(cum, i_idx, j_idx):
    if i_idx == 1:
        return cum[j_idx - 1]
    return cum[j_idx - 1] - cum[i_idx - 2]


if __name__ == "__main__":
    N = int(input())
    N_list = [int(i) for i in input().split(" ")]
    M = int(input())
    cum = [N_list[0]]
    for value in N_list[1:]:
        cum.append(cum[-1] + value)
    for _ in range(M):
        tmp = input().split(" ")
        i_idx, j_idx = int(tmp[0]), int(tmp[1])
        print(solution(cum, i_idx, j_idx))
