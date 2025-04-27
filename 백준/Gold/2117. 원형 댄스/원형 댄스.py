import sys
input = sys.stdin.readline

def solve(n: int) -> int:
    if n % 2 == 0:
        k = n // 2
        return k * (k - 1)
    else:
        k = (n - 1) // 2
        return k * k

def main():
    # 입력
    n = int(input().strip())
    # 풀이
    result = solve(n)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
