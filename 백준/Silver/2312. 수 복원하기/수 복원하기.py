import sys
input = sys.stdin.readline

def solve(T, nums):
    MAXN = 100000
    sieve = bytearray(b"\x01") * (MAXN + 1)
    sieve[0:2] = b"\x00\x00"
    primes = []
    for i in range(2, MAXN + 1):
        if sieve[i]:
            primes.append(i)
            step = i
            start = i * i
            if start <= MAXN:
                sieve[start:MAXN + 1:step] = b"\x00" * (((MAXN - start) // step) + 1)

    out = []
    for n in nums:
        x = n
        for p in primes:
            if p * p > x:
                break
            if x % p == 0:
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                out.append(f"{p} {cnt}")
        if x > 1:
            out.append(f"{x} 1")
    return out

def main():
    # 입력
    T = int(input().strip())
    nums = [int(input().strip()) for _ in range(T)]

    # 풀이
    result = solve(T, nums)

    # 출력
    print("\n".join(result))

if __name__ == "__main__":
    main()
