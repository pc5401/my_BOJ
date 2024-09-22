import sys
import collections
input = sys.stdin.readline


def solve(x: int, graph:collections.defaultdict[dict], memo: collections.defaultdict, basic: set) -> tuple:
    rtn = { b:0 for b in basic }

    for y, k in graph[x].items():
        if y in rtn:
            rtn[y] += k
            continue

        elif not y in memo:
            memo[y] = solve(y, graph, memo, basic)
        
        for i, cnt in memo[y].items():
            rtn[i] += cnt * k

    return rtn



def main():
    # 입력값
    N = int(input())
    M = int(input())
    graph = collections.defaultdict(dict)
    basic = { i for i in range(N)}

    for _ in range(M):
        X, Y, K = map(int, input().split())
        graph[X-1][Y-1] = K
        if X-1 in basic:
            basic.remove(X-1) 
    
    # 풀이
    memo = collections.defaultdict(dict)
    memo[N-1] = solve(N-1, graph, memo, basic)
    result = sorted(list(memo[N-1].items()))

    # 출력
    for i, cnt in result:
        print(f'{i+1} {cnt}')


if __name__ == "__main__":
    main()


