import sys
input = sys.stdin.readline


def solve(scores: list[int]) -> tuple[int, list[int]]:
    ranks = [(s, i) for i, s in enumerate(scores, start=1)]
    ranks.sort(key=lambda x: -x[0])

    total_score = 0
    numbers = []
    for i in range(5):
        score, num = ranks[i]
        total_score += score
        numbers.append(num)

    numbers.sort()
    
    return total_score, numbers


def main():
    # 입력값
    scores: list[int] = [int(input()) for _ in range(8)]

    # 풀이
    result = solve(scores)
    
    # 출력
    print(result[0])
    print(*result[1])

    
if __name__ == "__main__":
    main()