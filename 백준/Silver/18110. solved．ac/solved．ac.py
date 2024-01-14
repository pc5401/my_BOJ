import sys
input = sys.stdin.readline


def solve(n: int, lst: list) -> int:
    if not n:
        return 0
    
    EPS = 1e-9 # 매우 작은 수
    ex = round(n * 0.15 + EPS)
    return round(sum(lst[ex:n-ex]) / (n - 2*ex) + EPS)
        

if __name__ == "__main__":
    N = int(input())
    if N:
        lst = [int(input()) for _ in range(N)]
        lst.sort()
    else:
        lst = []
    print(solve(N, lst))
