if __name__ == '__main__':
    N = int(input())
    a, b, res = 1, 2, 0
    if N == 1:
        print(a)
    elif N == 2:
        print(b)
    else:
        for _ in range(N-2):
            c = a+b
            a = b % 10
            b = c % 10
        print(b)