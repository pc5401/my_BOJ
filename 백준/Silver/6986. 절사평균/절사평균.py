import sys
from decimal import Decimal, getcontext, ROUND_HALF_UP

input = sys.stdin.readline

# Decimal을 사용하기 위한 정밀도 설정
getcontext().prec = 10
getcontext().rounding = ROUND_HALF_UP

def trimmed_mean(n: int, k: int, scores: list[Decimal]) -> Decimal:
    return sum(scores) / (n - (2 * k))

def adjusted_mean(n: int, k: int, scores: list[Decimal]) -> Decimal:
    left_score = scores[0] * k
    right_score = scores[-1] * k
    sum_val = sum(scores) + left_score + right_score
    return sum_val / n

def main():
    N, K = map(int, input().split())
    scores: list[Decimal] = [Decimal(input()) for _ in range(N)]
    scores.sort()

    trimmed_mean_result = trimmed_mean(N, K, scores[K:N-K])
    adjusted_mean_result = adjusted_mean(N, K, scores[K:N-K])

    print(trimmed_mean_result.quantize(Decimal('0.01')))
    print(adjusted_mean_result.quantize(Decimal('0.01')))

if __name__ == "__main__":
    main()
