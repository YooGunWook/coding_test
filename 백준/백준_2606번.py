import collections

n = int(input())
m = int(input())

computer_connect = collections.defaultdict(list)
for _ in range(m):
    from_com, to_com = map(int, input().split(" "))
    computer_connect[from_com].append(to_com)
    computer_connect[to_com].append(from_com)


def recursive_dfs(v, discovered=[]):
    for w in computer_connect[v]:
        if w not in discovered:
            discovered.append(w)
            discovered = recursive_dfs(w, discovered)
    return discovered


print(len(recursive_dfs(1, discovered=[])) - 1)
