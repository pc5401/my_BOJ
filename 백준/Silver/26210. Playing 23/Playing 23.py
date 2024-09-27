import sys
input = sys.stdin.readline

def solve(N: int, john_cards: list, mary_cards: list, common_cards: list) -> int:
    # 카드의 점수 계산 함수
    def card_value(card):
        return card if 1 <= card <= 10 else 10

    # 사용된 카드 개수 추적
    used = [0] * 14  # 인덱스 1부터 13까지 사용

    # 초기 카드 사용 카운트 업데이트
    for card in john_cards + mary_cards + common_cards:
        used[card] += 1

    # 현재 존과 메리의 총점 계산
    john_total = sum(card_value(card) for card in john_cards + common_cards)
    mary_total = sum(card_value(card) for card in mary_cards + common_cards)

    min_card_needed = -1

    # 가능한 카드 값(1부터 13까지) 중에서 메리가 이길 수 있는 최소값 찾기
    for c in range(1, 14):
        if used[c] < 4:
            v = card_value(c)
            john_new_total = john_total + v
            mary_new_total = mary_total + v

            # 플레이어의 버스트 여부 확인
            john_bust = john_new_total > 23
            mary_bust = mary_new_total > 23

            # 메리가 승리하는 조건 확인
            mary_wins = False
            if mary_new_total == 23:
                mary_wins = True
            elif not mary_bust and john_bust:
                mary_wins = True

            if mary_wins:
                min_card_needed = c
                break  # 최소값을 찾았으므로 종료

    return min_card_needed

def main():
    # 입력값
    N = int(input())
    john_cards = list(map(int, input().split()))
    mary_cards = list(map(int, input().split()))
    common_cards = list(map(int, input().split()))

    # 풀이
    result = solve(N, john_cards, mary_cards, common_cards)

    # 출력
    print(result)

if __name__ == "__main__":
    main()