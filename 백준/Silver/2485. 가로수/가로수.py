import sys
input = sys.stdin.readline

def gcd(a, b):
    # 최대 공약수 찾는 gcd
    while b:
        a, b = b, a % b
    return a

def solve(n: int, trees: list) -> int:
    # 간격 구하기
    gaps = [trees[i+1] - trees[i] for i in range(n-1)]

    # 간격들의 최대공약수 계속 찾음
    g = gaps[0]
    for gap in gaps[1:]:
        g = gcd(g, gap)

    answer = sum([(gap // g) - 1 for gap in gaps])
    return answer

if __name__ == "__main__":
    N = int(input())
    trees = [int(input()) for _ in range(N)]
    print(solve(N, trees))
