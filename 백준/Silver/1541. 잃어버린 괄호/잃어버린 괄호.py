import sys
input = sys.stdin.readline


def num_and_order(string: str) -> tuple:
    v = ''
    num = []
    for w in string:
        if w == '+':
            num.append(int(v))
            num.append('+')
            v = ''
        elif w == '-':
            num.append(int(v))
            num.append('-')
            v = ''
        else:
            v += w
    
    num.append(int(v))
    return num

if __name__ == "__main__":
    sik = input().rstrip()
    num =  num_and_order(sik)
    i, n = 0, len(num)
    lst = [num[0]]
    
    while i < n:
        if num[i] == '+':
            a = lst.pop()
            b = num[i+1]
            lst.append(a+b)
            i += 2
        elif num[i] == '-':
            lst.append(num[i+1])
            i += 2
        else:
            i += 1
    
    res = lst.pop(0)
    while lst:
        res -= lst.pop(0)
    print(res)
