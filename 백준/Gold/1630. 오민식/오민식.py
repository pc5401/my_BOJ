import sys
input = sys.stdin.readline

MOD = 987654321

def solve(N):
    if N == 1:
        return 1
    sieve = bytearray(b"\x01") * (N + 1)
    sieve[0:2] = b"\x00\x00"
    primes = []
    lim = int(N ** 0.5)
    for i in range(2, N + 1):
        if sieve[i]:
            primes.append(i)
            if i <= lim:
                start = i * i
                step = i
                sieve[start:N + 1:step] = b"\x00" * (((N - start) // step) + 1)
    res = 1
    for p in primes:
        v = p
        while v * p <= N:
            v *= p
        res = (res * (v % MOD)) % MOD
    return res

def main():
    # 입력
    N = int(input().strip())

    # 풀이
    result = solve(N)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
