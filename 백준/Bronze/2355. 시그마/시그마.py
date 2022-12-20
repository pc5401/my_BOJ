a, b = map(int,input().split())
n = max(a,b) - min(a,b) + 1
res = ((a+b)*n)/2
print(int(res))