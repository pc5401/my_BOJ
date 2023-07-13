import sys
input = sys.stdin.readline

if __name__ == '__main__':
    x = int(input())
    res = 0

    while x:
        res += x & 1
        x = x >> 1

    print(res)