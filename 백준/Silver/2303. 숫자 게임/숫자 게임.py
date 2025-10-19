import sys
from itertools import combinations

def best_last_digit(cards):
    mx = -1
    for a, b, c in combinations(cards, 3):
        v = (a + b + c) % 10
        if v > mx:
            mx = v
    return mx

def solve(players):
    best_idx = 1
    best_val = -1
    for i, cards in enumerate(players, start=1):
        val = best_last_digit(cards)
        if val >= best_val:
            best_val = val
            best_idx = i
    return best_idx

def main():
    data = sys.stdin.read().strip().split()
    # 입력
    it = iter(data)
    N = int(next(it))
    players = [[int(next(it)) for _ in range(5)] for _ in range(N)]
    # 풀이
    ans = solve(players)
    # 출력
    print(ans)

if __name__ == "__main__":
    main()
