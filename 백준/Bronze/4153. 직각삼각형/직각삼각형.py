import sys
input = sys.stdin.readline

while 1:
    a,b,c = map(int,input().split())
    lst = [a,b,c]
    lst.sort()
    v = lst[2]*lst[2]
    x = lst[0]*lst[0] + lst[1]*lst[1]
    if a == 0 and b == 0 and c == 0:
        break

    if v == x:
        print('right')
    else:
        print('wrong')
