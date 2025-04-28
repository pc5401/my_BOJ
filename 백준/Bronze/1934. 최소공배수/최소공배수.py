import sys
import math
input = sys.stdin.readline

def solve(pairs: list[tuple[int, int]]) -> list[int]:
    res = []
    for a, b in pairs:
        g = math.gcd(a, b)
        res.append(a // g * b)
    return res

def main():
    # 입력
    T = int(input())
    pairs = [tuple(map(int, input().split())) for _ in range(T)]
    # 풀이
    result = solve(pairs)
    # 출력
    print("\n".join(map(str, result)))

if __name__ == "__main__":
    main()
