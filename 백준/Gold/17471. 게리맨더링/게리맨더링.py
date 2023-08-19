import sys
input = sys.stdin.readline


# 조합 계산
def combi(n: int):
    lst = []
    for i in range(1, 1 << N):
        a, b = [], []
        for j in range(N):
            if (i & (1<<j)):
                a.append(j+1)
            else:
                b.append(j+1)

        lst.append([a,b])
    lst.pop()
    return lst


def not_connect(A: list) -> bool:
    global N
    
    # 방문 확인 표
    visit = [0] * (N+1)
    for a in A:
        visit[a] = 1
    
    # 그래프 이동 DFS
    que = [A[0]]
    visit[A[0]] = 0
    while que:

        v = que.pop()
        for i in graph[v]:

            if visit[i]:
                visit[i] = 0
                que.append(i)

    if sum(visit): # 연결 안 됨.
        return True
    else: # 연결 됨
        return False


def search_min_value(x: list, y: list):
    global min_value
    
    # 연결 확인
    if not_connect(x) or not_connect(y):
        return
    
    # 차이 계산 및 확인
    x_cnt, y_cnt = 0, 0
    for i in x:
        x_cnt += population[i]

    for i in y:
        y_cnt += population[i]

    # 결과값 계산 및 수정
    min_value = min(min_value, abs(x_cnt - y_cnt))


if __name__ == '__main__':
    # 입력값 처리
    N = int(input())
    population = [0] + list(map(int,input().split()))
    graph = {}
    for i in range(1, N+1):
        graph[i] = list(map(int,input().split()))[1:]

    # 결과값 및 계산 
    min_value = float('INF')
    for x, y in combi(N):
        search_min_value(x,y)


    # 출력
    print( -1 if min_value == float('INF') else min_value)