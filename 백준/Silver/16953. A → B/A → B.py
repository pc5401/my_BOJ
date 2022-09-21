from collections import deque

a, b = map(int, input().split())

q = deque()
q.append([a, 0])
res = -2
cnt = 0
if a == b:
    print(0)
    quit()

while q:

    value = q.popleft()
    v = value[0]
    cnt = value[1] + 1
    # 오른쪽 추가
    l = int(str(v) + '1')
    V = v*2

    if v > 10e9:
        continue

    if b == l or b == V:
        res = cnt
        break

    else:
        q.append([l,cnt])
        q.append([V,cnt])

print(res+1)
