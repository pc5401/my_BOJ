import sys
input = sys.stdin.readline


def solve(N: int):
    rtn, n = N, N
    
    while (n>1):
        rtn = max(rtn ,n)
        if (n % 2):
            n *= 3
            n += 1
        else:
            n //=2
    
    return rtn



def main():
    T = int(input())
    lst = [int(input()) for _ in range(T)]
    result = [solve(v) for v in lst]
    for res in result:
        print(res)

main()
