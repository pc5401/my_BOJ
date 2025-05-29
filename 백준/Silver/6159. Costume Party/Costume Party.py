import sys
input = sys.stdin.readline

def solve(N: int, S: int, L: list[int]) -> int:
    lst = sorted(L)
    cnt = 0

    l, r = 0, N-1

    while l < r:
        if lst[l] + lst[r] <= S:
            cnt += (r - l)
            l += 1
        else:
            r -= 1

    return cnt



def main():
    # 입력
    N, S = map(int, input().split())
    L = [int(input()) for _ in range(N)]

    # 풀이
    result = solve(N, S, L)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
