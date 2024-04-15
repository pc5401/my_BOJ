import sys
input = sys.stdin.readline


def main():
    # 입력값
    chef = [sum(map(int, input().split())) for _ in range(5)]

    winner_num = 0
    winner_score = 0

    for num, score in enumerate(chef, start=1):
        if score > winner_score:
            winner_num = num
            winner_score = score

    print(winner_num, winner_score)


if __name__ == "__main__":
    main()