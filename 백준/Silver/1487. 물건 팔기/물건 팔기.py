import sys
input = sys.stdin.readline


def get_income(price: int, demands: list[int]) -> int:
    ans = 0
    for a, b in demands:
        if a >= price:
            profit_each = price - b
            if profit_each > 0:
                ans += profit_each
    return ans


def solve(N: int, demands: list[int]) -> int:
    ans = 0
    max_income = 0
    for price, b in demands:
        income = get_income(price, demands)

        if income > max_income:
            max_income = income
            ans = price
        elif income == max_income and price < ans:
            ans = price
    return ans


def main():
    # 입력값
    N = int(input())
    demands = [list(map(int, input().split())) for  _ in range(N)]
    
    result = solve(N, demands)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
