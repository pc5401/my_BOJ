import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int ,input().split())
    table = [[0]*N for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        table[a-1][b-1] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if table[i][k] and table[k][j]:
                    table[i][j] = 1


    res = 0
    for i in range(N): # 학생 순회
        cnt = 0
        for j in range(N): # 해당 학생 방문 가능
            cnt += 1 if table[i][j] or table[j][i] else 0
        
        if cnt == N-1:
            res += 1
    print(res)