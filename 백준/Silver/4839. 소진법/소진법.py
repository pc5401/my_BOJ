import sys

def next_prime(primes):
    if not primes:
        return 2
    x = primes[-1] + 1
    while True:
        is_p = True
        for p in primes:
            if p * p > x:
                break
            if x % p == 0:
                is_p = False
                break
        if is_p:
            return x
        x += 1

def solve(n):
    orig = n
    digits = []
    primes = []
    while n > 0:
        if not primes:
            p = 2
            primes.append(p)
        else:
            p = next_prime(primes)
            primes.append(p)
        digits.append(n % p)
        n //= p
    terms = []
    if digits:
        prefix = []
        for i, a in enumerate(digits):
            if a == 0:
                continue
            if i == 0:
                terms.append(str(a))
            else:
                if i > len(prefix):
                    prefix = [str(primes[j]) for j in range(i)]
                terms.append(str(a) + "*" + "*".join(prefix))
    else:
        terms.append("0")
    return f"{orig} = " + " + ".join(terms)

def main():
    #입력
    input = sys.stdin.readline
    nums = []
    while True:
        line = input().strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        nums.append(n)
    #풀이
    out_lines = [solve(n) for n in nums]
    #출력
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
