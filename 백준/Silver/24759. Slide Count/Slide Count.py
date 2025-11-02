import sys

def solve(N, C, w):
    diff = [0]*(N+1)
    s, e = 0, 0
    curr = w[0] if N > 0 else 0
    while s < N:
        if s <= e:
            diff[s] += 1
            diff[e+1] -= 1
        if e+1 >= N:
            if s <= e:
                curr -= w[s]
            s += 1
            if s > e:
                curr = 0
        elif curr + w[e+1] > C:
            if s <= e:
                curr -= w[s]
            s += 1
            if s > e:
                curr = 0
        else:
            e += 1
            curr += w[e]
    ans = [0]*N
    run = 0
    for i in range(N):
        run += diff[i]
        ans[i] = run
    return ans

def main():
    #입력
    input = sys.stdin.readline
    N, C = map(int, input().split())
    w = list(map(int, input().split()))
    #풀이
    ans = solve(N, C, w)
    #출력
    print(*ans, sep="\n")

if __name__ == "__main__":
    main()
