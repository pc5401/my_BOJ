import sys
import collections
input = sys.stdin.readline

def solve(n:int) -> int:
    lst = [0] * (N+1)
    Q = collections.deque()
    Q.append(n)

    while Q:
        v = Q.popleft()
        for i in data[v]:
            if lst[i]:
                continue
            lst[i] = lst[v] + 1
            Q.append(i)
    return sum(lst)

if __name__ == "__main__":
    # input 값
    N, M = map(int,input().split())
    data = collections.defaultdict(list)
    for m in range(M):
        a, b = map(int,input().split())
        data[a].append(b)
        data[b].append(a)
    # 세팅 값
    res = 0
    minV = 1e9
    # 풀이 시작
    for num in range(1,N):
        value = solve(num)
        if value < minV:
            minV = value
            res = num

    print(res)