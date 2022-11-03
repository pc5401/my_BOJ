while True:
    N = input()
    if N == '0':
        break
    v = len(N) + 1

    for n in N:
        if n == '1':
            v += 2
        elif n == '0':
            v += 4
        else:
            v += 3

    print(v)