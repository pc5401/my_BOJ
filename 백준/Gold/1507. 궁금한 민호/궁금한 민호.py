import sys
input = sys.stdin.readline

def solve(n: int, dist: list[list[int]]) -> int:
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or i == k or j == k:
                    continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    return -1

    total = 0
    used = [[False]*n for _ in range(n)]

    # i < j 
    for i in range(n):
        for j in range(i+1, n):
            redundant = False
            for k in range(n):
                if k == i or k == j:
                    continue
                if dist[i][j] == dist[i][k] + dist[k][j]:
                    redundant = True
                    break
            if not redundant:
                total += dist[i][j]
                used[i][j] = used[j][i] = True

    return total

def main():
    # 입력
    n = int(input())
    dist = [list(map(int, input().split())) for _ in range(n)]

    # 풀이
    result = solve(n, dist)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
