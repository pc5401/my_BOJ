if __name__ == '__main__':
    a = int(input())
    v = input().rstrip()
    b = int(input())

    if v == '*':
        print(a*b)
    elif v == '+':
        print(a+b)