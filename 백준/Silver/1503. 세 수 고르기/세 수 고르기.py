import sys
input = sys.stdin.readline

def solve(N: int, M: int, S: list[int]):
    rtn = float("inf")   

    lst = [n  for n in range(1, 1050) if not n in S]

    for x in lst:
        if rtn == 0:
            return 0
    
        for y in lst:
            for i in range(len(lst)):
                z = lst[i]
                val = abs(N-x*y*z)
                if i > 0 and val > abs(N-x*y*lst[i-1]):
                    break
                rtn = min(rtn, val)
                
    return rtn            



def main():
    N, M = map(int, input().split())
    if M != 0:
        S = set(map(int, input().split()))
        print(solve(N, M, S))
    else:
        print(0)

main()
