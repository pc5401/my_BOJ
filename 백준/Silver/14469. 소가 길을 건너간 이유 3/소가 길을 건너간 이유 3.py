import sys
input = sys.stdin.readline

N = int(input())
lst = []
for n in range(N):
    lst.append(list(map(int,input().split())))
lst.sort(key=lambda x : x[0])
cnt = lst[0][0]
for i,j in lst:
    if cnt >= i:
        cnt += j
    else:
        cnt = i + j

print(cnt)