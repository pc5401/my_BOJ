import sys
input = sys.stdin.readline


if __name__ == '__main__':
    dp = [1, 2]
    while dp[-1] < 10**100:
        dp.append(dp[-1] + dp[-2])


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


