import sys
import collections
input = sys.stdin.readline

def solve(N: int, M: int, lst: list[int], graph: collections.defaultdict[int, list]) -> list[int]:
    rtn = []
    Q = collections.deque()

    for i in range(1, N+1):
        if lst[i] == 0:
            Q.append(i)
    
    while Q:
        std = Q.popleft()
        rtn.append(std)

        for i in graph[std]:
            lst[i] -= 1
            if lst[i] == 0:
                Q.append(i)
        
    return rtn[::-1]


def main():
    # 입력값
    N, M = map(int, input().split())
    lst = [0] * (N + 1) # 해당 학생보다 작은 학생 수
    grahp = collections.defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        lst[a] += 1
        grahp[b].append(a)

    # 풀이
    result = solve(N, M, lst, grahp)
    # 출력
    print(*result)


if __name__ == "__main__":
    main()

