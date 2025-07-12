import sys
input = sys.stdin.readline

def solve(x: int, y: int) -> int:
    while x > 0 or y > 0:
        if (x % 3) + (y % 3) != 1:
            return 0
        x //= 3
        y //= 3
    return 1

def main():
    # 입력
    x, y = map(int, input().split())
    # 풀이
    result = solve(x, y)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
