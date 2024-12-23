import sys
input = sys.stdin.readline

def solve(N: int, M: int, A: list[int]) -> int:
    counts = [0] * (M + 1)
    for num in A:
        counts[num] += 1
    return max(counts[1:])

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    result = solve(N, M, A)
    print(result)
