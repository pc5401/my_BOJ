import sys

def solve(N, X, Y, M, B):
    M.sort()
    B.sort()
    ans = 0
    for i in range(N):
        if B[i] >= M[i]:
            ans += (B[i] - M[i]) * X
        else:
            ans += (M[i] - B[i]) * Y
    return ans

def main():
    #입력
    input = sys.stdin.readline
    N, X, Y = map(int, input().split())
    M, B = [], []
    for _ in range(N):
        m, b = map(int, input().split())
        M.append(m)
        B.append(b)
    #풀이
    ans = solve(N, X, Y, M, B)
    #출력
    print(ans)

if __name__ == "__main__":
    main()
