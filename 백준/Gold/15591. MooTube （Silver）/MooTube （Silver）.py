from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def bfs(usado,video):
    global N

    visit = [0]*(N+1)
    visit[video] = 1
    Q = deque([video])
    cnt = -1

    while Q:
        v = Q.popleft()
        cnt += 1
        
        for i in graph[v]:
            
            if graph[v][i] >= usado and not visit[i]:
                visit[i] = 1
                Q.append(i)

    return cnt


if __name__ == "__main__":
    N, Q = map(int,input().split())
    graph = defaultdict(dict)

    for i in range(N-1):
        pi,qi,ri = map(int,input().split())
        graph[pi][qi] = ri
        graph[qi][pi] = ri

    for i in range(Q):
        ki, vi = map(int,input().split())
        print(bfs(ki,vi))

