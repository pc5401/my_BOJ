import sys
input = sys.stdin.readline


if __name__ == '__main__':
    W, H, X, Y, P = map(int, input().split())
    players = [tuple(map(int, input().split())) for _ in range(P)]
    R = H/2
    res = 0
    r = R**2


    for x, y in players:
        if (X-x)**2 + ((Y+R)-y)**2 <= r:
            res += 1
        elif ((X+W)-x)**2 + ((Y+R)-y)**2 <= r:
            res += 1
        elif X <= x <= X+W and Y <= y <= Y+H:
            res += 1
        
    print(res)