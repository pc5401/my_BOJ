import sys
input = sys.stdin.readline


def solve(c: int, d: int, word: str) -> int:
    dp = [float('inf')] * c
    dp[0] = 0
    for i in range(c):
        if dp[i] == float('inf'):
            continue
        for j in range(1, d + 2):
            if i + j < c and word[i + j] == '.':
                dp[i + j] = min(dp[i + j], dp[i] + 1)
    return dp[-1] if dp[-1] != float('inf') else 0


def main():
    # 입력값
    T = int(input())
    cd = []
    words = []
    for _ in range(T):
        cd.append(tuple(map(int, input().split())))
        words.append(input().strip())
    
    # 풀이
    result = []
    for day in range(T):
        res = [f'Day #{day + 1}', f'{cd[day][0]} {cd[day][1]}', words[day]]
        res.append(solve(*cd[day], words[day]))
        result.append(res)
    
    # 출력
    for res in result:
        for r in res:
            print(r)
        print()

if __name__ == "__main__":
    main()
