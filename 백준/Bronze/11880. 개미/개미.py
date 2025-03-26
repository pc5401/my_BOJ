import sys
input = sys.stdin.readline

def solve(a: int, b: int, c: int) -> int:
    d1 = (a + b) * (a + b) + c * c
    d2 = (a + c) * (a + c) + b * b
    d3 = (b + c) * (b + c) + a * a
    result = min(d1, d2, d3)
    return result

def main():
    # 입력
    T = int(input().strip())
    for _ in range(T):
        a, b, c = map(int, input().split())
        # 풀이
        result = solve(a, b, c)
        # 출력
        print(result)

if __name__ == "__main__":
    main()
