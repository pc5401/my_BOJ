import sys
input = sys.stdin.readline


def main():
    # 입력값
    x1, x2 = map(int, input().split())
    a, b, c, d, e = map(int, input().split())
    
    # 풀이
    def integral(x):
        return (a / 3) * x**3 + (b - d) / 2 * x**2 + (c - e) * x

    result = int(integral(x2) - integral(x1))
    # 출력
    print(result)


if __name__ == "__main__":
    main()
