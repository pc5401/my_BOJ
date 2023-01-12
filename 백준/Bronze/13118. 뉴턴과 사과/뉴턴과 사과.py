p = list(map(int, input().split()))
x,y,r = map(int, input().split())
res = 0
for i in range(1,5):
    if p[i-1] == x:
        res = i
        
print(res)