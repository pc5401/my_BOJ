import sys
input = sys.stdin.readline

def solve(T, nums):
    out = []
    for N in nums:
        d = len(str(N))
        out.append("YES" if (N * N) % (10 ** d) == N else "NO")
    return out

def main():
    # 입력
    T = int(input().strip())
    nums = [int(input().strip()) for _ in range(T)]

    # 풀이
    result = solve(T, nums)

    # 출력
    print("\n".join(result))

if __name__ == "__main__":
    main()
