import sys
input = sys.stdin.readline

def isPossible(a: str , b: str) -> bool:
    if a == '0' or b == '0':
        return False
    return 10 < int(a+b) <= 26


def solve(number: list[str]) -> int:
    n = len(number)
    if n == 0:
        return 0
    if number[0] == '0':
        return 0
    
    if n == 1:
        return 1
    if number[1] == '0' and int(number[0]) > 2:
        return 0
    
    dp = [0] * n
    
    dp[0] = 1
    dp[1] = dp[0] + isPossible(number[0], number[1])

    for i in range(2, n):
        if number[i] == '0':
            if number[i-1] == '1' or number[i-1] == '2':
                dp[i] = dp[i-2]
            else:
                return 0
        
        elif isPossible(number[i-1], number[i]):
            dp[i] = (dp[i-2] + dp[i-1]) % 1000000
        else:
            dp[i] = dp[i-1]
        

    return dp[-1]


def main():
    # 입력값
    number = list(input().rstrip())
    
    # 풀이
    result = solve(number)

    # 출력
    print(result)


if __name__ == "__main__":
    main()
