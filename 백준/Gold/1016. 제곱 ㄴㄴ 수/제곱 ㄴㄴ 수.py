import sys
import math
input = sys.stdin.readline

def solve(mn: int, mx: int) -> int:
    length = mx - mn + 1
    is_bad = [False] * length
    limit = int(math.isqrt(mx))
    for i in range(2, limit + 1):
        sq = i * i
        # 첫 번째 배수 찾기
        start = ((mn + sq - 1) // sq) * sq
        for v in range(start, mx + 1, sq):
            is_bad[v - mn] = True
    return is_bad.count(False)

def main():
    # 입력
    mn, mx = map(int, input().split())
    # 풀이
    result = solve(mn, mx)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
