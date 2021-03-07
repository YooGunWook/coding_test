from itertools import combinations


def solution(orders, course):
    res = []

    for i in course:
        cnt = 0
        tmp = []
        menu_or = {}
        max_val = 0
        for menu in orders:
            if len(menu) < i:
                continue
            lis_comb = combinations(menu, i)

            for j in lis_comb:
                if j in tmp:
                    continue
                count = 0
                for order in orders:
                    if i > len(order):
                        continue

                    tmp_count = 0

                    for k in j:
                        if k in order:
                            tmp_count += 1

                    if tmp_count == i:
                        count += 1
                if count >= 2:
                    menu_or[j] = count
                    tmp.append(j)
                    max_val = max(count, max_val)

        if not menu_or:
            continue
        cnt = max(max_val, cnt)
        for key in menu_or:
            if menu_or[key] == cnt:
                res.append("".join(sorted(key)))

    return sorted(set(res))


if __name__ == "__main__":
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
