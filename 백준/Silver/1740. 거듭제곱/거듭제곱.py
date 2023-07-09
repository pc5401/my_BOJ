import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input()) # 500_000_000_000 
    res = 0
    n = format(N,'b')[::-1]
    for i, v in enumerate(n):
        if v == '1':
            res += 3**i

    print(res)