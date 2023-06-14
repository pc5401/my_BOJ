import collections

N = collections.deque(input())
res = 0
while N:
    res += 1
    v = str(res)
    for i in v:
        if N and i == N[0]:
            N.popleft()

print(res)