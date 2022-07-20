N = int(input())
lst = list(map(int, input().split()))
M = int(input())

btm, top = 0, max(lst)
res = 0
while top >= btm:

    sumV = 0
    mid = (btm+top)//2

    for i in range(N):
        if lst[i] > mid:
            sumV += mid
        else:
            sumV += lst[i]
    
    if sumV <= M:
        btm = mid + 1
    else:
        top = mid - 1

res = top
print(res)
