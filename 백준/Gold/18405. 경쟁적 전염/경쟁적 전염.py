import sys
import collections
input = sys.stdin.readline

def foo(virus_num):
    new_lst = []

    while virus[virus_num]:
        i, j = virus[virus_num].pop()
        if arr[i][j] != virus_num:
            continue

        for d in delta:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < N and 0 <= nj < N and not arr[ni][nj]:
                arr[ni][nj] = virus_num
                new_lst.append([ni, nj])

    return new_lst



if __name__ == '__main__':
    N, K = map(int,input().split())
    arr = []
    virus = collections.defaultdict(list)
    for i in range(N):
        row = list(map(int,input().split()))
        for j in range(N):
            if row[j] > 0:
                virus[row[j]].append([i, j])
        arr.append(row)

    S, X, Y = map(int,input().split())
    delta = [[-1,0], [1,0], [0,-1], [0,1]]
    for s in range(S):
        for k in range(1,K+1):
            virus[k] = foo(k)

    print(arr[X-1][Y-1])