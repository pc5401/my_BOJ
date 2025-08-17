import sys
input = sys.stdin.readline

def solve(N, segs):
    starts = [0] * N
    ends = [0] * N
    for i in range(N):
        s, e = segs[i]
        starts[i] = s
        ends[i] = e
    starts.sort()
    ends.sort()

    i = j = 0
    cur = ans = 0
    while i < N or j < N:
        if j == N or (i < N and starts[i] < ends[j]):
            cur += 1
            if cur > ans:
                ans = cur
            i += 1
        else:
            cur -= 1
            j += 1
    return ans

def main():
    # 입력
    N = int(input().strip())
    segs = [tuple(map(int, input().split())) for _ in range(N)]

    # 풀이
    result = solve(N, segs)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
