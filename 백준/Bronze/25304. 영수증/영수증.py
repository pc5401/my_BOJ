import sys
input = sys.stdin.readline

X = int(input())
N = int(input())
cnt = 0
for n in range(N):
    a,b = map(int,input().split())
    cnt += (a*b)

res = 'No' if X-cnt else 'Yes'
print(res) 