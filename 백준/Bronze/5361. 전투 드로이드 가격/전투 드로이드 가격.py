if __name__ == '__main__':
    prices = [350.34, 230.9, 190.55, 125.3, 180.9]
    N = int(input())
    for i in range(N):
        lst = list(map(float,input().split()))
        res = 0.0
        for x,y in zip(prices, lst):
            res += x*y
        print(f'${res:.2f}')