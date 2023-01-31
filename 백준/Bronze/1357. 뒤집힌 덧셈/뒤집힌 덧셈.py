def Rev(n):
    return int(str(n)[::-1])

x,y = map(int,input().split())
print(Rev(Rev(x) + Rev(y)))