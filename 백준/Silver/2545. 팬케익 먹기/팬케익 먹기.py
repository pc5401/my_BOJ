import sys
import decimal
input = sys.stdin.readline


def solve(abc:list, d: int) -> int:
    
    while d >0 and abc[2] > 1:
        abc[2] -= 1
        d -= 1
        abc.sort()

    return abc[0] * abc[1] * abc[2]

if __name__ == '__main__':
    T = int(input())
    res = []
    for tc in range(T):
        null_input = input()
        lst = list(map(decimal.Decimal, input().split()))
        D = lst.pop()
        lst.sort()
        res.append(solve(lst, D))
    for r in res:
        print(r)