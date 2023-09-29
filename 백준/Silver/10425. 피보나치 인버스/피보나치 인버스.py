import sys
input = sys.stdin.readline


def fibo(target, dp) -> int:
    lo, hi = 0, 100_000
    
    while lo <= hi:
        mid = (lo + hi) // 2

        if dp[mid] < target:
            lo = mid + 1
        elif dp[mid] == target:
            return mid
        else:
            hi = mid - 1

    return hi

if __name__ == "__main__":
    # 입력 & 전처리
    T = int(input())
    dp = [0] * 100_001
    dp[1] = 1
    for i in range(2, 100_001):
        dp[i] = dp[i-1] + dp[i-2]
    
    for tc in range(T):
        print(fibo(int(input()), dp))