import sys
import math
input = sys.stdin.readline

def make_lst(n: int) -> list:
    rtn = [1]
    for i in range(2, 50001):
        v = i**2
        if v - rtn[-1] > n:
            rtn.append(v)
            break
        rtn.append(v)
    return rtn


if __name__ == "__main__":
    G = int(input())
    res = []
    lst = make_lst(G)
    
    lo, hi = 0, 1

    while hi < len(lst):
        v = lst[hi] - lst[lo]
        if v == G:
            res.append(math.sqrt(lst[hi]))
            lo += 1
        elif v < G:
            hi += 1
        else:
            lo += 1

    if res: 
        for r in map(int, res): 
            print(r)
    else:
        print(-1)