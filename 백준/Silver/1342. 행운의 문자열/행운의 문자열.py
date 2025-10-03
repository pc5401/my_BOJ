import sys
from collections import Counter
from functools import lru_cache
input = sys.stdin.readline

def solve(S):
    cnt = Counter(S)
    chars = list(cnt.keys())
    init = tuple(cnt[c] for c in chars)
    m = len(chars)

    @lru_cache(maxsize=None)
    def dp(state, last):
        if not any(state):
            return 1
        total = 0
        for i in range(m):
            if state[i] and i != last:
                lst = list(state)
                lst[i] -= 1
                total += dp(tuple(lst), i)
        return total

    return dp(init, -1)

def main():
    # 입력
    S = input().strip()

    # 풀이
    result = solve(S)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
