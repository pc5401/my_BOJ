import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    tips = [int(input()) for _ in range(N)]
    tips.sort(key=lambda x:-x)

    res = 0
    for rank, tip in enumerate(tips, start=1):
        money = tip + 1 - rank
        if money > 0:
            res += money
        else:
            break
    
    print(res)
