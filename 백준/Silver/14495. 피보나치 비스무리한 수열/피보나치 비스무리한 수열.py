import sys
input = sys.stdin.readline

def solve(n):
    if n <= 3:
        return 1
    f = [0] * (n + 1)
    f[1] = f[2] = f[3] = 1
    for i in range(4, n + 1):
        f[i] = f[i - 1] + f[i - 3]
    return f[n]

def main():
    # 입력
    n = int(input().strip())

    # 풀이
    result = solve(n)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
