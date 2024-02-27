import sys
input = sys.stdin.readline

def find_maxmum_profit(n: int, prices: list)-> int:
    total_profit = 0
    day_max_price = [(n-1, prices[-1])]

    for day in range(n-2, -1, -1):
        price = prices[day]
        if price > day_max_price[-1][1]:
            day_max_price.append((day, price))
    
    start = 0
    while day_max_price:
        day, max_price = day_max_price.pop()
        for i in range(start, day):
            total_profit += (max_price - prices[i])

        start = day+1

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