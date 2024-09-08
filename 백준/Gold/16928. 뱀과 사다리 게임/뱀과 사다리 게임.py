import sys
import collections
input = sys.stdin.readline

def solve(N: int, M: int, ladders: dict[int, int], snakes: dict[int, int]) -> int:
    Q = collections.deque()
    Q.append((1, 0))
    visited = [1000] * (101)
    visited[0] = 0
    visited[1] = 0

    while Q:
        num, cnt = Q.popleft()
        if num > 100:
            continue
        
        if visited[num] < cnt:
            continue
        
        visited[num] = cnt

        if num in ladders:
            Q.append((ladders[num], cnt))
            continue
        elif num in snakes:
            Q.append((snakes[num], cnt))
            continue
        
        for i in range(1, 7):
            Q.append((num+i, cnt+1))
    
    return visited[100]


def main():
    # 입력값
    N, M = map(int, input().split())
    ladders = dict()
    snakes = dict()
    for _ in range(N):
        x, y = map(int, input().split())
        ladders[x] = y

    for _ in range(M):
        u, v = map(int, input().split())
        snakes[u] = v

    # 풀이
    result = solve(N, M, ladders, snakes)
    # 출력
    print(result)


if __name__ == "__main__":
    main()