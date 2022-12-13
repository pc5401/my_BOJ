import math

N = int(input())
lst = list(map(int,input().split()))
v = int(input())
cnt = 0

for i in lst:
    cnt += math.ceil(i/v)

print(cnt*v)