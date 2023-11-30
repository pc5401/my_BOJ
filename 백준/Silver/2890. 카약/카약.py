import sys
input = sys.stdin.readline


if __name__ == "__main__":
    R, C = map(int, input().split())
    photo = [list(map(lambda x: int(x) if x.isdigit() else 0 ,input().rstrip())) for _ in range(R)]
    rank_data = [[0, i] for i in range(10)]
    for j in range(C-2, 3, -1):
        for i in range(R):
            if photo[i][j]:
                rank_data[photo[i][j] - 1][0] = j
                photo[i][j], photo[i][j-1], photo[i][j-2] = 0, 0, 0

    rank_data.sort(key=lambda x : -x[0])
    res = [1] * 9
    rank = 1
    for i in range(1, 9):
        if rank_data[i][0] != rank_data[i-1][0]:
            rank += 1
        res[rank_data[i][1]] = rank

    for r in res:
        print(r)

