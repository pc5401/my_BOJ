import sys
import itertools
input = sys.stdin.readline

def get_lst(n: int) -> list[int]:
    rtn = [1]
    for i in range(1, n):
        r = rtn[-1] * i
        if r > n:
            return rtn
        rtn.append(r)        
    return rtn


def solve(n: int, lst: list[int]) -> str:
    if n == 0:
        return 'NO'
    elif n <= 4:
        return 'YES'

    m = len(lst)
    for i in range(1, m+1):
        for nums in itertools.combinations(lst, i):
            if n == sum(nums):
                return 'YES'

    return 'NO'

def main():
    N = int(input())
    lst: list[int] = get_lst(N)
    result = solve(N, lst)

    print(result)

        
if __name__ == '__main__':
    main()