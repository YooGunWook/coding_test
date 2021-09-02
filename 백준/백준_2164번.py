import collections

n = int(input())
queue = collections.deque()
for i in range(1, n+1):
    queue.append(i)
    
while len(queue) != 1:
    queue.popleft()
    card = queue.popleft()
    queue.append(card)

print(queue[0])