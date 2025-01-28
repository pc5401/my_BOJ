import sys
import collections
input = sys.stdin.readline


def solve(N: int, S: list[int]) -> list[int]:
    lst = [0] * (N+1)
    graph = collections.defaultdict(list)

    for s in S:
        for i in range(len(s) - 1):
            a = s[i]
            b = s[i + 1]
            graph[a].append(b)
            lst[b] += 1
    
    rtn = []
    Q = collections.deque()

    for i in range(1, N+1):
        if lst[i] == 0:
            Q.append(i)
    
    while Q:
        curr = Q.popleft()
        rtn.append(curr)

        for i in graph[curr]:
            lst[i] -= 1
            if lst[i] == 0:
                Q.append(i)
    if len(rtn) < N:
        return []
    return rtn
    

def main():
    # 입력
    N, M = map(int, input().split())
    S = [list(map(int, input().split()))[1:] for _ in range(M)]

    # 풀이
    result = solve(N, S)
    
    # 출력
    if not result:      # 사이클이어서 정렬 불가
        print(0)
    else:
        for res in result:
            print(res)

if __name__ == "__main__":
    main()
