import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext
input = sys.stdin.readline

def solve(N, M, K, lines):
    getcontext().prec = 50
    best = [Decimal('-Infinity')] * (N + 1)
    for line in lines:
        tok = line.split()
        for j in range(0, 2 * N, 2):
            i = int(tok[j])
            s = Decimal(tok[j + 1])
            if s > best[i]:
                best[i] = s
    top = sorted(best[1:], reverse=True)[:K]
    total = sum(top, Decimal(0))
    return total.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

def main():
    # 입력
    N, M, K = map(int, input().split())
    lines = [input().strip() for _ in range(M)]

    # 풀이
    result = solve(N, M, K, lines)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
