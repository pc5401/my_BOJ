import sys
from itertools import combinations
input = sys.stdin.readline

def len_val(a:list, b:list) -> float:
    return (b[0]-a[0])**2 + (b[1]-a[1])**2

def solve(lst:list) -> int:
    comb = list(combinations(lst, 2))
    dists = sorted([len_val(i, j) for i, j in comb])

    if len(set(dists[:4])) == 1 and len(set(dists[4:])) == 1:
        return 1
    else:
        return 0


if __name__ == "__main__":
    T:int = int(input())
    for tc in range(T):
        input_lst:list = sorted([list(map(int,input().split())) for i in range(4)])
        print(solve(input_lst))
