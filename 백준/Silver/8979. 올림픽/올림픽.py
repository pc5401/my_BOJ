import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort(key=lambda x: (-x[1], -x[2], -x[3]))
    ranks = [1] * N
    k_rank = 0
    for i in range(1, N):
        if lst[i][1] == lst[i-1][1] and lst[i][2] == lst[i-1][2] and lst[i][3] == lst[i-1][3]:
            ranks[i] = ranks[i-1]
        else:
            ranks[i] = i + 1
        
        if lst[i][0] == K:
            k_rank = ranks[i]

    if lst[0][0] == K:
        k_rank = ranks[0]

    print(k_rank)
