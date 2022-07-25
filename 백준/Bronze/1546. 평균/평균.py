n = int(input())
lst = list(map(int, input().split()))

m = max(lst)
res = [0] * n

for i in range(n):
    res[i] = lst[i]/m*100

print(sum(res)/n)