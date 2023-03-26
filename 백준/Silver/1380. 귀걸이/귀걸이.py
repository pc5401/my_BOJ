import sys
input = sys.stdin.readline

res = []
while True:
    n = int(input())
    if not n:
        break
    
    names = [""] * (n+1)
    check = [2] * (n+1)
    for name in range(1,n+1):
        names[name] = input()
    
    for _ in range(2*n -1):
        a,v = input().split()
        num = int(a)
        if check[num] > 0:
            check[num] -= 1
    res.append(names[check.index(1)])

for i,r in enumerate(res,start=1):
    print(i, r, end='')