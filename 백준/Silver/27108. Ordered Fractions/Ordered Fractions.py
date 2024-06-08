import sys
from math import gcd
input = sys.stdin.readline


def solve(N: int) -> list[str]:
    numbers = [(0, 1, 0),(1, 1, 1)]
    
    for i in range(1, N+1):
        for j in range(1, i):
            if gcd(j, i) == 1:
                numbers.append((j/i, i, j))

    numbers = sorted(numbers, key=lambda x: x[0])
    rtn = [f'{j}/{i}' for x, i, j in numbers]
    return rtn


def main():
    N: int = int(input())
    result: list[str] = solve(N)
    print(len(result))
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
