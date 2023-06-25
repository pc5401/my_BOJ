import sys
input = sys.stdin.readline

def plus(n: int):
    if n == 0:
        print(0)
        print(0)
    elif n < 3:
        print(1)
        print(1)
    else:
        a, b, res = 0, 1, 1
        for i in range(n-1):
            res = a + b
            a = b
            b = res
        print(1)
        print(res%1000000000)

def minus(n: int):
    v = n * -1
    if v == 1:
        print(1)
        print(1)
    elif v == 2:
        print(-1)
        print(1)
    else:
        a, b, res = 0, 1, -1
        for i in range(v-1):
            res = a - b
            a = b
            b = res
        print(1 if res > 0 else -1)
        print(abs(res)%1000000000)

if __name__ == '__main__':
    N = int(input())
    if N >= 0:
        plus(N)
    else:
        minus(N)
