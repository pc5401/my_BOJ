import sys
input = sys.stdin.readline


def solve(N: int, K: int):
    dp = [1] * (N+1)
    cnt = 0

    for i in range(2, N+1):
        if dp[i]:
            for p in range(i, N+1, i):
                if not dp[p]:
                    continue
                cnt += 1
                dp[p] = 0

                if cnt == K:
                    return p

    return p
    

def main():
    # 입력값
    N, K = map(int, input().split())

    # 결과 출력
    print(solve(N, K))

        
if __name__ == '__main__':
    main()