import sys
input = sys.stdin.readline

def solve(N):
    def digit_sum_odd(x):
        return sum(int(c) for c in str(x)) % 2 == 1

    is_absolute = (N == 4 or N >= 6) and digit_sum_odd(N)

    MAX = 2700
    spf = list(range(MAX + 1))
    for i in range(2, int(MAX ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, MAX + 1, i):
                if spf[j] == j:
                    spf[j] = i

    def distinct_prime_factors(x):
        cnt = 0
        last = -1
        while x > 1:
            p = spf[x]
            if p != last:
                cnt += 1
                last = p
            x //= p
        return cnt

    is_lim = False
    if N in (2, 4):
        is_lim = True
    else:
        if N > 1:
            dcnt = distinct_prime_factors(N)
            is_composite = dcnt >= 1 and not (dcnt == 1 and N == spf[N])  # quick prime check fails for prime powers; fix below
            # refine: x is prime if dcnt==1 and spf[N]==N; composite if not prime and N>1
            is_prime = (dcnt == 1 and spf[N] == N)
            is_composite = (not is_prime and N > 1)
            if is_composite and dcnt % 2 == 0:
                is_lim = True

    if is_absolute and is_lim:
        return 4
    if is_absolute:
        return 1
    if is_lim:
        return 2
    return 3

def main():
    # 입력
    N = int(input().strip())

    # 풀이
    result = solve(N)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
