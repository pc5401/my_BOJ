import sys
import collections
input = sys.stdin.readline


def solve(N: int) -> list[int]:
    rtn = [] # 버린 카드
    cards = collections.deque( i for i in range(1, N+1))

    while cards:
        rtn.append(cards.popleft()) # 버림
        if cards:# 밑으로
            card = cards.popleft()
            cards.append(card)

    return rtn


def main():
    # 입력값
    N: int = int(input())

    # 풀이
    result: list[int] = solve(N)

    # 출력
    print(*result)
    

if __name__ == "__main__":
    main()
