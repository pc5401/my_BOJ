if __name__ == '__main__':
    lst = [list(map(int,input().split())) for _ in range(3)]
    X = [ x[0] for x in lst]
    Y = [ y[1] for y in lst]
    res = []
    for i in X:
        if X.count(i) == 2:
            continue
        res.append(i)
    
    for j in Y:
        if Y.count(j) == 2:
            continue
        res.append(j)
    
    print(*res)
