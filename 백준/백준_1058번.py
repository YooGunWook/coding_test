# n = int(input())
# friends_list = [list(input().strip()) for _ in range(n)]

# 플로이드 알고리즘 기반 풀이
def find_friend(n, friend_list):
    list_visit = [[0] * n for _ in range(n)] * 3
    result = 0
    for k in range(n):  # 경유지 -> 친구의 친구를 찾을 때 활용
        for i in range(n):  # 서로 친구인지 탐색
            for j in range(n):  # 서로 친구인지 탐색
                if i == j:
                    continue
                if friend_list[i][j] == "Y" or (
                    friend_list[i][k] == "Y" and friend_list[k][j] == "Y"
                ):
                    list_visit[i][j] = 1
    for person in range(n):  # visit 수를 이용해서 합을 구한다.
        result = max(result, sum(list_visit[person]))  # 가장 높은 값을 가진 친구가 제일 인싸
    return result


if __name__ == "__main__":
    n = 3
    friends_list = [["N", "Y", "Y"], ["Y", "N", "Y"], ["Y", "Y", "N"]]
    print(find_friend(n, friends_list))