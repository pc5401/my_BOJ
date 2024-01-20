import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    X = list(map(int, input().split()))
    idx_X = [ [i, v] for i, v in enumerate(X) ]
    idx_X.sort(key=lambda x : x[1])
    
    # 원래값 삭제 및 rank 기록
    rank = 0
    lst = [0]
    for i in range(1, N):
        if idx_X[i][1] == idx_X[i-1][1]:
            lst.append(i)
        else:
            while lst:
                idx_X[lst.pop()][1] = rank
            lst.append(i)
            rank += 1

    while lst:
        idx_X[lst.pop()][1] = rank

    idx_X.sort(key=lambda x : x[0])
    res = [x[1] for x in idx_X]
    print(*res)