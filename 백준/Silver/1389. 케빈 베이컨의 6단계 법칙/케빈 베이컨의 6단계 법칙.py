import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    network = [[1e9]*N for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        network[A-1][B-1] = 1
        network[B-1][A-1] = 1

    for k in range(N):
        network[k][k] = 0
        for i in range(N):
            for j in range(N):
                if network[i][j] > network[i][k] + network[k][j]:
                    network[i][j] = network[i][k] + network[k][j]

    res = 0
    sumV = 1e9
    for i in range(N):
        value = sum(network[i])
        if sumV > value:
            res = i
            sumV = value
    
    print(res+1)

