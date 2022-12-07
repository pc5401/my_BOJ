N = int(input())
lst = list(map(int,input().split()))
arr = [0]*(101)
res = 0

for i in lst:
    if arr[i]:
        res += 1
        continue

    arr[i] = 1

print(res)