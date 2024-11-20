import sys
input = sys.stdin.read

def solve(p: list[int]):
    n: int = p[0]
    lst: list[int] = p[1:]

    dp = [0] * (n - 1)

    for i in range(n - 1):
        v = abs(lst[i] - lst[i + 1])
        if v >= n:
            return 'Not jolly'
        
        dp[v - 1] += 1
    
    if all(dp):
        return 'Jolly'
    return 'Not jolly'


if __name__ == "__main__":
    # 입력값
    problems = input().strip().split("\n")
    problems = [list(map(int, line.split())) for line in problems]

    # 풀이
    result = [solve(problem) for problem in problems]

    # 출력
    for res in result:
        print(res)
