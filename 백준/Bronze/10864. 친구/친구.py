import sys
input = sys.stdin.readline

def solve(N, pairs):
    deg = [0] * (N + 1)
    for a, b in pairs:
        deg[a] += 1
        deg[b] += 1
    return deg[1:]

def main():
    # 입력
    N, M = map(int, input().split())
    pairs = [tuple(map(int, input().split())) for _ in range(M)]

    # 풀이
    result = solve(N, pairs)

    # 출력
    print("\n".join(map(str, result)))

if __name__ == "__main__":
    main()
