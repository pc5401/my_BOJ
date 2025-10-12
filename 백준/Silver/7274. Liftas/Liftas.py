import sys
input = sys.stdin.readline

def solve(N, K, A):
    total = sum(A)
    A.sort(reverse=True)
    skip = sum(A[:K]) if K > 0 else 0
    return total - skip

def main():
    # 입력
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    # 풀이
    ans = solve(N, K, A)
    # 출력
    print(ans)

if __name__ == "__main__":
    main()
