import sys
input = sys.stdin.readline


def solve(n: int, dp: list) -> int:
    l = len(dp)
    if n < l:
        return dp[n]
    
    for i in range(l, n+1):
        dp.append((dp[i-2] + dp[i-4] + dp[i-6]) % 1_000_000_009)

    return dp[n]



def main():
    # 입력값
    T = int(input())
    dp = [1, 1, 2, 2, 3, 3, 6]
    
    # 풀이
    result = [solve(int(input()), dp) for _ in range(T)]

    # 출력
    for res in result:
        print(res)


if __name__ == "__main__":
    main()
