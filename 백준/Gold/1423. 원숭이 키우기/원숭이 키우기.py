import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def solve(N: int, D: int, A: list[int], B: list[int]) -> int:
    basePower = 0
    for i in range(N):
        basePower += A[i] * B[i]
    dp = [[[-1] * 105 for _ in range(N)] for _ in range(105)]
    
    def getDp(leftDays, levelIdx, accumCnt):
        if levelIdx == N - 1:
            return 0
        if dp[leftDays][levelIdx][accumCnt] != -1:
            return dp[leftDays][levelIdx][accumCnt]
        ret = 0
        maxPossible = accumCnt + A[levelIdx]
        for i in range(maxPossible + 1):
            if leftDays < i:
                break
            ret = max(
                ret,
                getDp(leftDays - i, levelIdx + 1, i) + (B[levelIdx + 1] - B[levelIdx]) * i
            )
        dp[leftDays][levelIdx][accumCnt] = ret
        return ret

    return basePower + getDp(D, 0, 0)


if __name__=="__main__":
    # 입력
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    D = int(input())

    # 풀이
    result = solve(N, D, A, B)
    
    # 출력
    print(result)
