import sys
input = sys.stdin.readline
from functools import lru_cache

@lru_cache(maxsize=None)
def ways(num, total, min_val):
    if num == 0:
        return 1 if total == 0 else 0
    if num == 1:
        return 1 if total >= min_val else 0
    cnt = 0
    for a in range(min_val, total + 1):
        if a * num > total:
            break
        cnt += ways(num - 1, total - a, a)
    return cnt

def solve(num, total, min_val, kth):
    if num == 1:
        return [total]
    for a in range(min_val, total + 1):
        if a * num > total:
            break
        cnt = ways(num - 1, total - a, a)
        if kth <= cnt:
            return [a] + solve(num - 1, total - a, a, kth)
        kth -= cnt
    return []


def main():
    # 입력
    n, m, k = map(int, input().split())
    
    # 풀이
    result = solve(n, m, 1, k)
    
    # 출력
    print(*result)

if __name__ == "__main__":
    main()
