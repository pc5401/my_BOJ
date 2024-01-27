import sys
input = sys.stdin.readline


if __name__ == '__main__':
    L = int(input())
    string = list(map(lambda x : ord(x)-96, list(input().rstrip())))
    r, m = 31, 1234567891
    H = sum([string[i]*(r**i) for i in range(L)]) % m
    print(H)
