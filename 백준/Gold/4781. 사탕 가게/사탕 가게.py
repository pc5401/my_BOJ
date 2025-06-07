import sys
input = sys.stdin.readline

def solve(n: int, money_cents: int, candies: list[tuple[int,int]]) -> int:
    dp = [0] * (money_cents + 1)
    for cal, cost in candies:
        for w in range(cost, money_cents + 1):
            val = dp[w - cost] + cal
            if val > dp[w]:
                dp[w] = val
    return dp[money_cents]

def main():
    # 입력
    while True:
        line = input().split()
        if not line:
            break
        n = int(line[0])
        if n == 0:
            break
        m = float(line[1])
        money_cents = int(round(m * 100))
        candies = []
        for _ in range(n):
            c, p = input().split()
            cal = int(c)
            price_cents = int(round(float(p) * 100))
            candies.append((cal, price_cents))
        # 풀이
        result = solve(n, money_cents, candies)
        # 출력
        print(result)

if __name__ == "__main__":
    main()
