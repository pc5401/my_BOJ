import sys
input = sys.stdin.readline

def solve(N, M, L):
    cnt = [0] * N
    cur = 0
    cnt[cur] = 1
    throws = 0
    if M == 1:
        return 0
    while cnt[cur] < M:
        if cnt[cur] % 2 == 1:
            nxt = (cur + L) % N
        else:
            nxt = (cur - L) % N
        throws += 1
        cur = nxt
        cnt[cur] += 1
    return throws

def main():
    # 입력
    N, M, L = map(int, input().split())
    # 풀이
    ans = solve(N, M, L)
    # 출력
    print(ans)

if __name__ == "__main__":
    main()

    