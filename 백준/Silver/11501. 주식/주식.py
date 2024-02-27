import sys
input = sys.stdin.readline

def find_maxmum_profit(n: int, prices: list)-> int:
    total_profit = 0
    max_price = prices[-1]

    for day in range(n-2, -1, -1):
        price = prices[day]
        if price > max_price:
            max_price = price
            continue
        total_profit += (max_price -price)

    return total_profit

if __name__ == '__main__':
    T = int(input())
    res = []
    for _ in range(T):
        N = int(input())
        prices = list(map(int, input().split()))
        res.append(find_maxmum_profit(N, prices))

    for r in res:
        print(r)