import sys
input = sys.stdin.readline

def solve(N, M, A):
    ps = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        row = ps[i]
        prow = ps[i-1]
        ai = A[i-1]
        s = 0
        for j in range(1, M+1):
            s += ai[j-1]
            row[j] = prow[j] + s

    def rect(x1, y1, x2, y2):
        return ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1]

    ans = 0

    for c1 in range(1, M-1):
        for c2 in range(c1+1, M):
            s1 = rect(1, 1, N, c1)
            s2 = rect(1, c1+1, N, c2)
            s3 = rect(1, c2+1, N, M)
            v = s1 * s2 * s3
            if v > ans:
                ans = v

    for r1 in range(1, N-1):
        for r2 in range(r1+1, N):
            s1 = rect(1, 1, r1, M)
            s2 = rect(r1+1, 1, r2, M)
            s3 = rect(r2+1, 1, N, M)
            v = s1 * s2 * s3
            if v > ans:
                ans = v

    for c in range(1, M):
        for r in range(1, N):
            s1 = rect(1, 1, N, c)
            s2 = rect(1, c+1, r, M)
            s3 = rect(r+1, c+1, N, M)
            v = s1 * s2 * s3
            if v > ans:
                ans = v

            s1 = rect(1, 1, r, c)
            s2 = rect(r+1, 1, N, c)
            s3 = rect(1, c+1, N, M)
            v = s1 * s2 * s3
            if v > ans:
                ans = v

    for r in range(1, N):
        for c in range(1, M):
            s1 = rect(1, 1, r, M)
            s2 = rect(r+1, 1, N, c)
            s3 = rect(r+1, c+1, N, M)
            v = s1 * s2 * s3
            if v > ans:
                ans = v

            s1 = rect(1, 1, r, c)
            s2 = rect(1, c+1, r, M)
            s3 = rect(r+1, 1, N, M)
            v = s1 * s2 * s3
            if v > ans:
                ans = v

    return ans

def main():
    # 입력
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        s = input().strip()
        if len(s) == M and all(ch.isdigit() for ch in s):
            A.append(list(map(int, s)))
        else:
            A.append(list(map(int, s.split())))

    # 풀이
    result = solve(N, M, A)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
