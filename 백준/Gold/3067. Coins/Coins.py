import sys
input = sys.stdin.readline


def solve(n: int, coins: list[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1 
    
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    
    return dp[target]


def main():
    # 입력값
    T = int(input())
    number_of_coin = []
    type_of_coin = []
    M = []

    for _ in range(T):
        number_of_coin.append(int(input()))
        type_of_coin.append(list(map(int, input().split())))
        M.append(int(input()))

    # 풀이
    result = [solve(number_of_coin[i], type_of_coin[i], M[i]) for i in range(T)]

    # 출력
    for res in result:
        print(res)


if __name__ == "__main__":
    main()


