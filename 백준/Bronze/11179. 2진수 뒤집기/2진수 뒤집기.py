import sys
input = sys.stdin.readline

def solve(n: int) -> int:
    b = bin(n)[2:]
    return int(b[::-1], 2)

def main():
    # 입력
    n = int(input().strip())
    # 풀이
    result = solve(n)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
