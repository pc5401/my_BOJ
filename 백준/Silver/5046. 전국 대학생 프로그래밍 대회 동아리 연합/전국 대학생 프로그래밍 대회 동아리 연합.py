import sys
input = sys.stdin.readline


def solve(N: int, B: int, H: int, costs: list[int], vacancys: list[list[int]]) -> int:
    total = float('INF')
    
    for h in range(H):
        for week in vacancys[h]:
            if week >= N and costs[h] * N <= B:
                total = min(costs[h] * N, total)

    return total

def main():
    # 입력값
    costs, vacancys = [], []
    N, B, H, W = map(int, input().split())
    for _ in range(H):
        costs.append(int(input()))
        vacancys.append(list(map(int, input().split())))
    
    # 풀이
    result: int= solve(N, B, H, costs, vacancys)

    # 출력

    print(result if result != float('INF') else 'stay home')

if __name__ == "__main__":
    main()