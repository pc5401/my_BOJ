import sys
input = sys.stdin.readline

N = int(input())
res = []
for _ in range(N):
    s = list(input())
    s[0] = s[0].upper()
    res.append("".join(s))

for r in res:
    print(r, end="")