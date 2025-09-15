import sys
import math
input = sys.stdin.readline

def solve(N):
    root = int(math.isqrt(N))
    end = max(2, root)

    best_sum = 10**18
    for a in range(2, end + 1):
        b = (N + a - 1) // a
        if b < 2:
            b = 2
        s = a + b
        if s < best_sum:
            best_sum = s

    a = max(2, root + 1)
    b = (N + a - 1) // a
    if b < 2:
        b = 2
    s = a + b
    if s < best_sum:
        best_sum = s

    return 2 * (best_sum - 2)

def main():
    # 입력
    N = int(input().strip())

    # 풀이
    result = solve(N)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
