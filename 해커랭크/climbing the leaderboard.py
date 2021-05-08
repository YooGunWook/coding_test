import bisect


def climbingLeaderboard(ranked, player):  # 이분 탐색으로 진행
    rank_dict = {}  # rank를 담는 dictionary
    ranking = 1  # 일등부터 담는다
    for i in ranked:  # 무조건 sorting되어 있음
        if i not in rank_dict:
            rank_dict[i] = ranking
            ranking += 1
    ranked.sort()  # 이분 탐색을 위해 inverse
    ans = []
    for score in player:
        index = bisect.bisect_right(ranked, score)  # 오른쪽을 기준으로 탐색 진행
        if index == len(ranked):  # 만약 길이랑 같게 나오면 최상위로 올라간거임
            ans.append(rank_dict[ranked[index - 1]])
            continue
        if index == 0:  # 꼴찌를 의미함
            ans.append(rank_dict[ranked[index]] + 1)
            continue
        ans.append(rank_dict[ranked[index - 1]])  # 그 외 친구들을 넣어준다.

    return ans


print(
    climbingLeaderboard(
        list(map(int, input().split(" "))), list(map(int, input().split(" ")))
    )
)
