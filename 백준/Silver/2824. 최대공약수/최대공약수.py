import sys
input = sys.stdin.readline

MOD = 10**9

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            is_prime[start:limit + 1:step] = [False] * (((limit - start) // step) + 1)
    return [i for i, v in enumerate(is_prime) if v]

_PRIMES = sieve(31623)

def factorize(x):
    res = {}
    n = x
    for p in _PRIMES:
        if p * p > n:
            break
        if n % p == 0:
            cnt = 0
            while n % p == 0:
                n //= p
                cnt += 1
            res[p] = cnt
    if n > 1:
        res[n] = res.get(n, 0) + 1
    return res

def solve(N, arrA, M, arrB):
    cntA = {}
    cntB = {}

    for a in arrA:
        if a == 1:
            continue
        fa = factorize(a)
        for p, c in fa.items():
            cntA[p] = cntA.get(p, 0) + c

    for b in arrB:
        if b == 1:
            continue
        fb = factorize(b)
        for p, c in fb.items():
            cntB[p] = cntB.get(p, 0) + c

    res_mod = 1
    truncated = False
    res_big = 1

    for p, ca in cntA.items():
        cb = cntB.get(p, 0)
        c = ca if ca < cb else cb
        if c == 0:
            continue
        res_mod = (res_mod * pow(p, c, MOD)) % MOD
        if not truncated:
            for _ in range(c):
                res_big *= p
                if res_big >= MOD:
                    truncated = True
                    res_big = None
                    break

    if truncated:
        return f"{res_mod:09d}"
    else:
        return str(res_big)

def main():
    # 입력
    N = int(input().strip())
    arrA = list(map(int, input().split()))
    M = int(input().strip())
    arrB = list(map(int, input().split()))
    # 풀이
    ans = solve(N, arrA, M, arrB)
    # 출력
    print(ans)

if __name__ == "__main__":
    main()
