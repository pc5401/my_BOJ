import sys, math
input = sys.stdin.readline

def solve(n: int, x: int, amplitudes: list[int]) -> list[float]:
    s = sum(a * a for a in amplitudes)
    if s == 0:
        return amplitudes
    c = math.sqrt(x * n / s)
    return [f'{a * c:.10f}' for a in amplitudes]

def main():
    # 입력
    n, x = map(int, input().split())
    amplitudes = list(map(int, input().split()))
    
    # 풀이
    result = solve(n, x, amplitudes)
    
    # 출력
    print(*result)

if __name__ == "__main__":
    main()
