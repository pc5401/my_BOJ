if __name__ == '__main__':
    a, b, c = map(int, input().split())
    sumV = [0] * 100

    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                sumV[i+j+k] += 1

    res = 0
    maxV = 0

    for idx, val in enumerate(sumV):
        if val > maxV:
            maxV = val
            res = idx

    print(res)