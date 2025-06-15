import sys
input = sys.stdin.readline

def solve(N: int, K: int, breeds: list[int]) -> int:
    last_pos = {}
    ans = -1
    for i, b in enumerate(breeds):
        if b in last_pos and i - last_pos[b] <= K:
            if b > ans:
                ans = b
        last_pos[b] = i
    return ans

def main():
    # 입력
    N, K = map(int, input().split())
    breeds = [int(input()) for _ in range(N)]
    # 풀이
    result = solve(N, K, breeds)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
