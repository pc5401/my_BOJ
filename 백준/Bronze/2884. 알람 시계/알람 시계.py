H, M = map(int,input().split())

h = H
m = M - 45

if m < 0:
    h = H - 1 if h > 0 else 23
    m = 60 + m

print(h, m)