def solve(r: int, c: int) -> tuple[int, int]:
    total_cards = r * c
    pairs = total_cards // 2

    min_actions = pairs
    max_actions = total_cards - 1

    return min_actions, max_actions


def main():
    # 입력
    r, c = map(int, input().split())

    # 풀이
    min_turns, max_turns = solve(r, c)

    # 출력
    print(min_turns, max_turns)


if __name__ == "__main__":
    main()
