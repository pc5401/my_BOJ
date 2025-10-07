import sys
import math
input = sys.stdin.readline

def solve(n):
    return math.isqrt(n)

def main():
    # 입력
    n = int(input().strip())

    # 풀이
    side = solve(n)

    # 출력
    print(f"The largest square has side length {side}.")

if __name__ == "__main__":
    main()
