import sys
input = sys.stdin.readline

def up(n):
    V = str(n)
    res = ''
    for v in V:
        if v == '5':
            res += '6'
        else:
            res += v
    return int(res)

def down(n):
    V = str(n)
    res = ''
    for v in V:
        if v == '6':
            res += '5'
        else:
            res += v
    return int(res)

x,y = map(int,input().split())

A,B = up(x), up(y)
a,b = down(x), down(y)

print((a+b),(A+B))