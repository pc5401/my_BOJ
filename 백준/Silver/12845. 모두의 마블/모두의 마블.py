import sys
input = sys.stdin.readline

def solve(n, L):
    if n == 1:
        return 0
    mx = max(L)
    return sum(L) + (n - 2) * mx

def main():
    # 입력
    n = int(input().strip())
    L = list(map(int, input().split()))

    # 풀이
    result = solve(n, L)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
