def cal(n):
    for i in range(2*n, 1100000, n):
        lst[i] = 0
    

a = int(input())
lst = [1] * (1100000)
res = 0

for i in range(2,1100000):
    if lst[i]:
        cal(i)

for i in range(a, 1100000):
    if lst[i]:
        v = str(i)
        if v == v[::-1]:
            res = i
            break
        

print(res if res > 1 else 2)