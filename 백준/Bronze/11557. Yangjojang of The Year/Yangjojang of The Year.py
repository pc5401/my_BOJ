T = int(input())
for tc in range(T):
    N = int(input())
    res = ''
    maV = 0
    for n in range(N):
        inpu = list(input().split())
        v = int(inpu[1])
        if v > maV:
            maV = v
            res = inpu[0]

        
    print(res)