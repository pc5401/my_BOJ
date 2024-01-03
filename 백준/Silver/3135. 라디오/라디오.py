import sys
input = sys.stdin.readline

if __name__ == "__main__":
    A, B = map(int,input().split())
    N = int(input())
    buttons = [int(input()) for _ in range(N)]
    buttons.sort()
    now = A
    res = 0
    for button in buttons:
        if abs(B - button) < abs(B - now):
            now = button
    
    if now != A:
        res += 1
    
    res += abs(B - now)
    print(res)