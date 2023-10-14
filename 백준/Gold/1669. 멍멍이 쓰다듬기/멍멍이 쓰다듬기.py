if __name__ == "__main__":
    # 입력 & 전처리
    X, Y = map(int, input().split())
    number = abs(X - Y)
    n = 0
    while n*(n+1) - number < 0: 
        n += 1
    # print(number, n)
    if number == n*(n+1):
        print(2*n)
    elif n*(n+1) - number < n:
        print(2*n)
    else:
        print(2*(n-1) + 1)
