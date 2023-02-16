import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    J = [['J']*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == n-1) or (j == 0 or j == n-1):
                J[i][j] ='#'
    
    for i in range(n):
        print("".join(J[i]))

    print()
    