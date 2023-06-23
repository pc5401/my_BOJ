import sys
input = sys.stdin.readline


if __name__ == '__main__':
    dp = [0] * 482
    dp[0], dp[1] = 1,2
    for i in range(2,482):
        dp[i] = dp[i-1] + dp[i-2]

    while True:
        a, b = map(int,input().split())
        if a == 0 and b == 0:
            break
        
        cnt = 0
        for d in dp:
            if d >= a and d <= b:
                cnt += 1

            if d >= b:
                break
    
        print(cnt)

