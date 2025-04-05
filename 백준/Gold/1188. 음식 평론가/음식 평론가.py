import sys
import math
input = sys.stdin.readline

def solve(N: int, M: int) -> int:
    return M - math.gcd(N, M)

def main():
    # 입력
    N, M = map(int, input().split())
    
    # 풀이
    result = solve(N, M)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
