import sys
input = sys.stdin.readline

def solve(N, X):
    X.sort()
    L = 2 * N
    S = [-1] * L
    used = [False] * N

    def dfs(pos):
        while pos < L and S[pos] != -1:
            pos += 1
        if pos == L:
            return True
        for i in range(N):
            if used[i]:
                continue
            v = X[i]
            j = pos + v + 1
            if j < L and S[j] == -1:
                used[i] = True
                S[pos] = S[j] = v
                if dfs(pos + 1):
                    return True
                used[i] = False
                S[pos] = S[j] = -1
        return False

    if dfs(0):
        return S
    return -1

def main():
    # 입력
    N = int(input().strip())
    X = list(map(int, input().split()))

    # 풀이
    result = solve(N, X)

    # 출력
    if result == -1:
        print(-1)
    else:
        print(*result)

if __name__ == "__main__":
    main()

