import sys
import collections
input = sys.stdin.read


def solve(N: int, tree: list[int]) -> tuple[int, int]:
    s = 0
    for i in range(N):
        if tree[i]:
            s = i
            break
        
    Q = [s] # dfs
    visited = [0] * N
    visited[s] = 1

    while Q:
        v = Q.pop()

        for i in tree[v]:
            if visited[i]:
                continue
            visited[i] = 1
            Q.append(i)

    s = visited[0]

    for i in range(1, N):
        if visited[i] != s:
            return (1, i+1)



if __name__ == "__main__":
    # 입력값
    data = input().split('\n')
    N = int(data[0])
    tree = collections.defaultdict(list)
    for i in range(1, N-1):
        x, y = map(int, data[i].split())
        tree[x-1].append(y-1)
        tree[y-1].append(x-1)

    # 풀이
    result = solve(N, tree)
    
    # 출력
    print(*result)