import sys
input = sys.stdin.readline

def solve(n, k, times):
    cnt = 0
    for i in range(1, n):
        if times[i - 1] - times[i] >= k:
            cnt += 1
    return cnt

def main():
    # 입력
    n, k = map(int, input().split())
    times = [int(input()) for _ in range(n)]

    # 풀이
    result = solve(n, k, times)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
