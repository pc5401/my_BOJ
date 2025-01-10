import sys
import functools
input = sys.stdin.read

@functools.cache
def w(a: int, b: int, c: int) -> int:
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    
    return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


def solve(lst: list[int]) -> list[str]:
    return [f'w({a}, {b}, {c}) = {w(a,b,c)}' for a, b, c in lst]


if __name__=="__main__":
    # 입력
    lst = [map(int, a.split()) for a in input().split('\n')]

    # 풀이
    result = solve(lst[:-2])
    
    # 출력
    for res in result:
        print(res)