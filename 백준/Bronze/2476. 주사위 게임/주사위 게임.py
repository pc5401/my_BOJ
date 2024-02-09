import sys
input = sys.stdin.readline

def abc(a: int,b: int,c: int) -> int:
    if a == b and b == c:
        return 10000 + a * 1000
    elif a == b:
        return 1000 + a * 100
    elif b == c:
        return 1000 + b * 100
    elif a == c:
        return 1000 + c * 100
    else:
        return max(a,b,c) * 100


if __name__ == '__main__':
    res = 0
    N = int(input())
    for _ in range(N):
        a, b, c = map(int, input().split())
        res = max(res, abc(a,b,c))
    
    print(res)