import sys
input = sys.stdin.readline

def get_lst(n: int) -> list[int]:
    rtn = [1]
    for i in range(1, n):
        r = rtn[-1] * i
        if r > n:
            return rtn[::-1]
        rtn.append(r)        
    
    return rtn[::-1]


def solve(n: int, lst: list[int]) -> str:
    if n == 0:
        return 0
    elif n <= 4:
        return 1

    for m in lst:
        if m <= n:
            n -= m
    
    return n == 0

def main():
    N = int(input())
    lst: list[int] = get_lst(N)
    result = solve(N, lst)

    print('YES' if result else 'NO')

        
if __name__ == '__main__':
    main()