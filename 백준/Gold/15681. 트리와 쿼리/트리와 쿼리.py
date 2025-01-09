import sys
import collections
input = sys.stdin.readline

sys.setrecursionlimit(10**7)


def solve(N, R, trees) -> list[int]:
    rtn = [0] * (N+1)

    def dfs(node, prev):
        rtn[node] = 1

        for nxt in trees[node]:
            if nxt == prev:
                continue
            dfs(nxt, node)
            rtn[node] += rtn[nxt]

    dfs(R, 0)

    return rtn



if __name__ == '__main__':
    # 입력값
    N, R, Q = map(int, input().split())
    trees = collections.defaultdict(list)
    for _ in range(N-1):
        u, v = map(int, input().split())
        trees[u].append(v)
        trees[v].append(u)
    
    U = [int(input()) for _ in range(Q)]

    result = solve(N, R, trees)

    [print(result[u]) for u in U]
    