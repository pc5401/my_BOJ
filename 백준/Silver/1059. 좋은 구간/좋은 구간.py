import sys
input = sys.stdin.readline

L = int(input())
S = list(map(int,input().split()))
n = int(input())
S.sort()
x, y = 0,0
for i,s in enumerate(S):
    if s == n:
        break
    elif s > n:
        x = S[i-1] if i-1 > -1 else 0
        y = S[i]
        break
# x ~ y 의 경우의 수
if x == 0 and y == 0: print(0)
else: print((x - n)*(n - y)-1)