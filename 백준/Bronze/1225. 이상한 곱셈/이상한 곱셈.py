import sys
input = sys.stdin.readline

a,b = input().split()

res = 0
for i in a:
    for j in b:
        x = int(i)
        y = int(j)
        res += x * y
print(res)