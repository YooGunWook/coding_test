from itertools import combinations

n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    mat.append(row)


def get_lowest(mat, n):
    team_count = int(n // 2)
    people = [i for i in range(n)]
    pair_list = list(combinations(people, team_count))
    print(pair_list)
    res = 100000
    for i in range(len(pair_list) - 1):
        pair = list(combinations(pair_list[i], 2))
        team1_scores = 0
        for score in pair:
            team1_scores += mat[score[0]][score[1]]
            team1_scores += mat[score[1]][score[0]]
        team2 = list(set(people) - set(pair_list[i]))
        team2_scores = 0
        team2_pair = list(combinations(team2, 2))
        for score in team2_pair:
            team2_scores += mat[score[0]][score[1]]
            team2_scores += mat[score[1]][score[0]]
        res = min(res, abs(team1_scores - team2_scores))
    print(res)


if __name__ == "__main__":
    get_lowest(mat, n)
