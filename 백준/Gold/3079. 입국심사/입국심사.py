import sys
input = sys.stdin.readline

def solve(N, M, T):
    left, right = 1, max(T) * M
    while left < right:
        mid = (left + right) // 2
        cnt = 0
        for t in T:
            cnt += mid // t
            if cnt >= M:
                break
        if cnt >= M:
            right = mid
        else:
            left = mid + 1
    return left

def main():
    # 입력
    N, M = map(int, input().split())
    T = [int(input()) for _ in range(N)]

    # 풀이
    result = solve(N, M, T)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
