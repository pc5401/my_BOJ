import sys
input = sys.stdin.readline

def opening(r:int, c:int) -> list:
    opening_union = []
    stack = [[r,c]]
    visit[r][c] = 1

    while stack:
        v = stack.pop()
        val = A[v[0]][v[1]]

        for d in ((0,-1),(1,0), (-1,0),(0,1)):
            nr = v[0] + d[0]
            nc = v[1] + d[1]
            if nr < N and nr >= 0 and nc < N and nc >= 0 and visit[nr][nc] == 0:
                value = abs(val - A[nr][nc])
                if value >= L and R >= value:
                    stack.append([nr, nc])
                    opening_union.append([nr, nc])
                    visit[nr][nc] = 1

    if opening_union:
        opening_union.append([r, c])

    return opening_union

def unions_opened():
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                continue
            union = opening(i,j)
            if union:
                unions.append(union)

def people_movement(lst:list):

    p = sum([A[i][j] for i,j in lst]) // len(lst)
    for i,j in lst: A[i][j] = p

if __name__ == "__main__":
    # input 값
    N, L, R = map(int,input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    # 풀이
    for res in range(2000+1):
        unions = []
        visit = [[0 for j in range(N)] for i in range(N)] # 방문 표시
        unions_opened()
        if not unions:
            break
        for uni in unions:
            people_movement(uni)
    
    print(res)