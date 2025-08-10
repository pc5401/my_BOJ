import sys
input = sys.stdin.readline

def solve(FF, FS, SF, SS):
    a, b, c, d = FF, FS, SF, SS
    if a + b == 0:
        return d + (1 if c > 0 else 0)
    if b == 0:
        return a
    return a + d + 2 * min(b, c) + (1 if b > c else 0)

def main():
    # 입력
    FF, FS, SF, SS = map(int, input().split())

    # 풀이
    result = solve(FF, FS, SF, SS)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
