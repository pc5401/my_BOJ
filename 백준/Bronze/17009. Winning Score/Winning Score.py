import sys
input = sys.stdin.readline

def solve(apple_scores: list[int], banana_scores: list[int]) -> str:
    a_total = apple_scores[0]*3 + apple_scores[1]*2 + apple_scores[2]*1
    b_total = banana_scores[0]*3 + banana_scores[1]*2 + banana_scores[2]*1
    if a_total > b_total:
        return 'A'
    if b_total > a_total:
        return 'B'
    return 'T'

def main():
    # 입력
    apple = [int(input().strip()) for _ in range(3)]
    banana = [int(input().strip()) for _ in range(3)]
    # 풀이
    result = solve(apple, banana)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
