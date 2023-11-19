import sys
input = sys.stdin.readline

def func(flag:int, lst:list):
    rtn = 0

    if flag: # positive:
        lst.sort()
    else: # negative
        lst.sort(key=lambda x:-x)

    while len(lst) > 1:
        a = lst.pop()
        b = lst.pop()
        if flag:
            if a == 1:
                lst.append(a)
                lst.append(b)
                return rtn
            elif b == 1:
                lst.append(b)
                rtn += a
                return rtn
        
        rtn += (a*b)
    
    return rtn


if __name__ == "__main__":
    N = int(input())
    positive = []
    negative = []
    zero = []
    res = 0

    for _ in range(N):
        n = int(input())
        if n > 0:
            positive.append(n)
        elif n < 0:
            negative.append(n)
        else:
            zero.append(n)

    res += func(1, positive)
    res += func(0, negative)

    if positive:
        res += sum(positive)
    
    if negative and not zero:
        res += negative.pop()

    print(res)