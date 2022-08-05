n = int(input())
lst = [1] * 10

for _ in range(n-1):
    for i in range(10):
        lst[i] = sum(lst[i:])

print(sum(lst)%10007)

