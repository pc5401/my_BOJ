import sys
input = sys.stdin.readline


def solve(n:int, lst:list) -> int:
    if n < 2:
        return sum(lst)
    
    dp = [0] * n
    dp[0], dp[1] = lst[0], max(lst[0],lst[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + lst[i])
    
    return dp[-1]

if __name__ == "__main__":
    T:int = int(input())
    for tc in range(T):
        input_lst:list = list(map(int,input().split()))
        print(solve(len(input_lst), input_lst))