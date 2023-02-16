import sys
input = sys.stdin.readline

gan = [1,2,3,3,4,10]
sa = [1,2,2,2,3,5,10]
T = int(input())
for tc in range(T):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    A = 0
    B = 0

    for i,v in enumerate(a):
        if v:
            A += gan[i] * v

    for i,v in enumerate(b):
        if v:
            B += sa[i] * v

    if A < B:
        print(f'Battle {tc+1}: Evil eradicates all trace of Good')
    elif A > B:
        print(f'Battle {tc+1}: Good triumphs over Evil')
    else:
        print(f'Battle {tc+1}: No victor on this battle field')