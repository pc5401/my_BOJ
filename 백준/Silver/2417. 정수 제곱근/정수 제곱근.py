n = int(input())

l = 0
r = n

cnt = 0
while l <= r:
    cnt += 1
    mid = ( l + r ) // 2

    if mid ** 2 < n:
        l = mid + 1
    else:
        r = mid - 1

print(mid if mid**2 >= n else mid+1)