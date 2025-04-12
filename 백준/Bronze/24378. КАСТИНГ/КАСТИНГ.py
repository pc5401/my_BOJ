import sys
input = sys.stdin.readline

def solve(mode: int, n: int, a: int, b: int, c: int) -> int:
    if mode == 1:
        return max(0, a + b + c - 2 * n)
    else:
        return min(a, b, c)

def main():
    # 입력
    mode = int(input().strip())
    n, a, b, c = map(int, input().split())
    
    # 풀이
    result = solve(mode, n, a, b, c)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
