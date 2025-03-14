import sys
input = sys.stdin.readline

def sieve(n: int) -> list[int]:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def factorize(num: int, primes: list[int]) -> tuple[int, int]:
    for p in primes:
        if p*p > num:
            break
        if num % p == 0:
            return p, num // p
    return num, 1

def solve(M: int, keys: list[int]) -> list[int]:
    primes_list = sieve(65536)
    fact_set = set()
    for key in keys:
        f1, f2 = factorize(key, primes_list)
        fact_set.add(f1)
        fact_set.add(f2)
    return sorted(fact_set)

def main():
    # 입력
    M = int(input().strip())
    keys = [int(input().strip()) for _ in range(M)]
    
    # 풀이
    ans = solve(M, keys)
    
    # 출력
    out_lines = []
    for i in range(0, len(ans), 5):
        out_lines.append(" ".join(map(str, ans[i:i+5])))
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()