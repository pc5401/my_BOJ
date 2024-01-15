import sys
input = sys.stdin.readline

def solve(cake: tuple) -> int:
    a, b, c, D = cake

    if D > 0:
        cut = [a, b, c]
        cut.sort() # 크기 순으로 a, b, c
        a, b, c = cut
        x = c - b
        if x >= D:
            return (c-D) * b * a
        D -= x
        c -= x
        # b, c 동일
        x = b - a
        if 2*x >= D:
            p, q = D//2, D%2
            return (c-p-q)*(b-p)*a
        c-= x
        b -= x
        D -= (2*x)
        # a, b, c 동일
        p, q = D//3, D%3
        a -= p
        b -= p 
        c -= p
        if q == 2:
            return (c-1)*(b-1)*a
        elif q == 1:
            return (c-1)*b*a
    
    return a*b*c



if __name__ == "__main__":
    T = int(input())
    lst = []
    for _ in range(T):
        input()
        lst.append(tuple(map(int,input().split())))
    
    res = []
    
    for i in lst:
        res.append(solve(i))
    
    for r in res:
        print(r)