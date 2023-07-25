if __name__ == "__main__":
    x, k = map(int,input().split())

    a = k + 2 * k + 4*k
    b = k / 2 + k + k * 2
    c = k / 4 + k / 2 + k

    if a <= x:
        print(int(a*1000))
    elif b <= x:
        print(int(b*1000))
    elif c <= x:
        print(int(c*1000))
    else:
        print(0)