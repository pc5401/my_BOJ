import sys

def solve(N, b):
    limit = (1 << (b + 1)) - 1
    return "yes" if N <= limit else "no"

def main():
    #입력
    N, b = map(int, sys.stdin.readline().split())
    #풀이
    ans = solve(N, b)
    #출력
    print(ans)

if __name__ == "__main__":
    main()
