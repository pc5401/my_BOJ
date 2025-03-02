import sys
input = sys.stdin.readline

def solve(n: int, m: int, A: list[int]) -> int:
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + A[i]
    ans = 0
    for i in range(n):
        if A[i] == m:
            L = i
            while L > 0 and A[L - 1] > m:
                L -= 1
            R = i
            while R < n - 1 and A[R + 1] > m:
                R += 1
            total = prefix[R + 1] - prefix[L]
            if total > ans:
                ans = total
    return ans

def main():
    # 입력
    t = int(input())
    results = []
    for _ in range(t):
        n, m = map(int, input().split())
        A = list(map(int, input().split()))
        # 풀이
        results.append(solve(n, m, A))
    # 출력
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
