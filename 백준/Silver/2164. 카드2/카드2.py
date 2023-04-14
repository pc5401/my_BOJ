from collections import deque

N = int(input())
cards = deque([i for i in range(1,N+1)])

while cards:
    v = cards.popleft()
    if cards:
        v = cards.popleft()
        cards.append(v)

print(v)