import sys
input = sys.stdin.readline      


def solve(price: int, option: list[int]) -> int:
    result = price
    
    for q, p in option:
        result += (q*p)
    
    return result
     

if __name__ == "__main__":
    # 입력값
    T = int(input())
    prices = []
    options = []
    for _ in range(T):
        prices.append(int(input()))
        n = int(input())
        options.append([tuple(map(int, input().split())) for _ in range(n)])

    # 풀이
    result = [solve(prices[t], options[t]) for t in range(T)]

    # 출력
    for res in result:
        print(res)