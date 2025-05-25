import sys
input = sys.stdin.readline

def solve(A: int) -> int:
    return A // 5

def main():
    # 입력
    A = int(input().strip())
    # 풀이
    result = solve(A)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
