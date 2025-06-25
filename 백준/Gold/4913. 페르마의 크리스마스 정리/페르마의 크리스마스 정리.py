import sys
input = sys.stdin.readline

def solve(queries: list[tuple[int,int]]) -> list[str]:
    MAX = 10**6
    is_prime = [True] * (MAX+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(MAX**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, MAX+1, i):
                is_prime[j] = False
    ps_prime = [0] * (MAX+1)
    ps_good = [0] * (MAX+1)
    cnt_p = cnt_g = 0
    for i in range(MAX+1):
        if is_prime[i]:
            cnt_p += 1
            if i == 2 or i % 4 == 1:
                cnt_g += 1
        ps_prime[i] = cnt_p
        ps_good[i] = cnt_g

    results = []
    for L, U in queries:
        l = max(L, 2)
        if l > U:
            x = y = 0
        else:
            x = ps_prime[U] - ps_prime[l-1]
            y = ps_good[U] - ps_good[l-1]
        results.append(f"{L} {U} {x} {y}")
    return results

def main():
    # 입력
    queries = []
    while True:
        L, U = map(int, input().split())
        if L == -1 and U == -1:
            break
        queries.append((L, U))
    # 풀이
    output = solve(queries)
    # 출력
    print("\n".join(output))

if __name__ == "__main__":
    main()
