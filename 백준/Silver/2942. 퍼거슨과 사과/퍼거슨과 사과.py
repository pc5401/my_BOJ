import sys
import math
input = sys.stdin.readline


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def get_divisor(n: int) -> list[int]:
    rtn = []
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            rtn.append(i)
            if i != n // i:
                rtn.append(n // i)
    rtn.sort()
    return rtn


def solve(R: int, G: int) -> list[list[int]]:
    n = gcd(R, G)
    lst = get_divisor(n)

    return [(i, R//i, G//i) for i in lst]

if __name__ == "__main__":
    # 입력값
    R, G = map(int, input().split())
    # 풀이
    result = solve(R, G)
    
    # 출력
    for res in result:
        print(*res)
