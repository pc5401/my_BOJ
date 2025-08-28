import sys
input = sys.stdin.readline

def solve(queries):
    maxN = max(queries)
    phi = list(range(maxN + 1))
    for p in range(2, maxN + 1):
        if phi[p] == p:
            for j in range(p, maxN + 1, p):
                phi[j] -= phi[j] // p

    pref = [0] * (maxN + 1)
    for i in range(1, maxN + 1):
        pref[i] = pref[i - 1] + phi[i]

    return [1 + 2 * pref[n] for n in queries]

def main():
    # 입력
    C = int(input().strip())
    queries = [int(input().strip()) for _ in range(C)]

    # 풀이
    result = solve(queries)

    # 출력
    print("\n".join(map(str, result)))

if __name__ == "__main__":
    main()
