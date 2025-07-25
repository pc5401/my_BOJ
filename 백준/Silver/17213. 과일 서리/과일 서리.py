import sys
input = sys.stdin.readline

def solve(k: int, n: int) -> int:
    if k < 0 or k > n:
        return 0
    
    k = min(k, n - k)
    num = 1
    den = 1
    for i in range(1, k+1):
        num *= n - k + i
        den *= i
    return num // den


def main():
    # 입력
    N = int(input().strip())
    M = int(input().strip())
    # 풀이
    result = solve(N-1, M-1)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
