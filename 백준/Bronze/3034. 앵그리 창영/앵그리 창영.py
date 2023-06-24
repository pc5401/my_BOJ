import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, x, y = map(int,input().split())
    v = x**2 + y**2
    res = []
    for i in range(N):
        l = int(input())
        if l**2 > v:
            res.append('NE')
        else:
            res.append('DA')
    for r in res:
        print(r)