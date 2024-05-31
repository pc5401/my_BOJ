import sys
import functools
input = sys.stdin.readline


@functools.cache
def solve(n: int, k: int) -> int:
    if n == 1 or n == 2:
        return 1
    elif k == 1:
        return 1
    elif n == k:
        return 1

    return solve(n-1, k-1) + solve(n-1, k)

def main():
    # 입력값
    n, k = map(int, input().split())
    # 풀이
    result: int = solve(n, k)
    # 출력
    
    print(result)
    
if __name__ == "__main__":
    main()

