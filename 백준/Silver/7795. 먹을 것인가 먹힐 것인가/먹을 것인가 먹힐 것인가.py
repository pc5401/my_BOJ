import sys
input = sys.stdin.readline

def func(n:int, lst:list, l):
    start, end = 0, l-1
    v = -1
    while start <= end:
        mid = (start + end) // 2

        if n > lst[mid]: # 왼쪽 이동 
            start = mid + 1
            v = mid
        else:
            end = mid - 1

    return v


T = int(input())
result = []
for tc in range(T):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    cnt = 0
    for i in range(N):
        cnt += func(A[i],B,M)+1
    result.append(cnt)

for r in result:
    print(r)