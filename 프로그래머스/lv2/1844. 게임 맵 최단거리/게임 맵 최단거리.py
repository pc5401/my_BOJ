import collections

def solution(maps):
    n, m = len(maps), len(maps[0])
    visit = [[0 for j in range(m)] for i in range(n)]
    
    Q = collections.deque()
    Q.append([0, 0])
    visit[0][0] = 1
    
    while Q:
        i,j = Q.popleft()
        
        for d in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < n and 0 <= nj < m and not visit[ni][nj] and maps[ni][nj] :
                Q.append([ni,nj])
                visit[ni][nj] = (visit[i][j] + 1)
                
    return visit[n-1][m-1] if visit[n-1][m-1] else -1