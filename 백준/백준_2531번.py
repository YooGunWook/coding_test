import collections

n, d, k, c = list(map(int, input().split(" ")))
chobab_list = []
for _ in range(n):
    chobab_list.append(int(input()))


def solution(n, d, k, c, chobab_list):
    max_count = 0
    chobab_list += chobab_list[: k + 2]
    eat_list = collections.deque([chobab_list[0]])

    for right in range(1, len(chobab_list)):
        eat_list.append(chobab_list[right])

        if len(eat_list) == k:
            if c not in eat_list:
                tmp_count = len(set(eat_list)) + 1
            else:
                tmp_count = len(set(eat_list))

            eat_list.popleft()
            max_count = max(tmp_count, max_count)

    return max_count


print(solution(n, d, k, c, chobab_list))

