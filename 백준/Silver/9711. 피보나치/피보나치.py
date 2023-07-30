import sys
input = sys.stdin.readline

def func(p: int) -> int:
    global N

    if dp[p]:
        return dp[p]
    
    for i in range(N, p+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    N = p+1
    return dp[p]

if __name__ == "__main__":
    dp = [0] * 10001
    dp[1], dp[2] = 1, 1
    N = 3
    res = []
    T =int(input())
    for tc in range(T):
        P, Q = map(int,input().split())
        res.append(func(P) % Q)
    
    for tc,r in enumerate(res,start=1):
        print(f'Case #{tc}: {r}')