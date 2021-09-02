n = int(input())
tokens = []
for _ in range(n):
    tokens.append(input())
tokens.sort(key=lambda x: len(x))
ans = 0
for idx in range(len(tokens)):
    head = tokens[idx]
    isHead = False
    for j in range(idx + 1, len(tokens)):
        if tokens[j].startswith(head):
            isHead = True
            break
    if not isHead:
        ans += 1
print(ans)
