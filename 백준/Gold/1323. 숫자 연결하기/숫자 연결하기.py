import sys
input = sys.stdin.readline

def solve(N, K):
    L = len(str(N))
    A = pow(10, L, K)
    B = N % K

    r = B
    t = 1
    visited = [False] * K if K > 0 else []

    while True:
        if r == 0:
            return t
        if visited[r]:
            return -1
        visited[r] = True
        r = (r * A + B) % K
        t += 1

def main():
    # 입력
    N, K = map(int, input().split())

    # 풀이
    result = solve(N, K)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
