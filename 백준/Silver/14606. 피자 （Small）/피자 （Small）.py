import sys
input = sys.stdin.readline


def solve(N: int):
    if N == 1:
        return 0
    
    dp = [0, 0, 1, 3, 6, 10]

    if N % 2:
        a, b = (N // 2) + 1, N // 2 
    else :
        a, b  = N // 2, N // 2
    return a*b + dp[a] + dp[b]



def main():
    N = int(input())
    print(solve(N))

main()


