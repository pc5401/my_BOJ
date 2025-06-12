import sys
from collections import Counter
input = sys.stdin.readline

def solve(cards: list[int]) -> int:
    cnt = Counter(cards)
    max_freq = max(cnt.values())
    return min(num for num, freq in cnt.items() if freq == max_freq)

def main():
    # 입력
    N = int(input().strip())
    cards = [int(input().strip()) for _ in range(N)]
    # 풀이
    result = solve(cards)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
