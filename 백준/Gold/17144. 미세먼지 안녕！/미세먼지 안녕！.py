import sys
input = sys.stdin.readline


def dusting(R: int, C:int, A:list) -> list:
    dusted_A = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if A[i][j] > 0: # 먼지 있으면,
                dust = A[i][j] // 5
                cnt = 0
                for d in [[0,1], [1,0],[-1,0],[0,-1]]: # 주변에 흩뿌리고
                    ni = i + d[0]
                    nj = j + d[1]
                    if 0 <= ni < R and 0 <= nj < C and A[ni][nj] != -1:
                        dusted_A[ni][nj] += dust
                        cnt += 1
                # 가운데 먼지 남는다.
                dusted_A[i][j] += (A[i][j] - dust * cnt)
    
    return dusted_A  # 참고! 공기청정기 -1 안 넣음


def air_cleaning(R: int, C: int, A: list, cleaner:list, delta: list):
    
    i, j, dir = cleaner[0], cleaner[1], 0
    ni, nj = 1, 1
    prev = A[i][j]

    while ni != cleaner[0] or nj != cleaner[1]:
        ni = i + delta[dir][0]
        nj = j + delta[dir][1]
        if 0 <= ni < R and 0 <= nj < C:
            next = A[ni][nj]
            A[ni][nj]  = prev
            prev = next
            i = ni
            j = nj
        else:
            dir += 1
            if dir > 3:
                break

    A[cleaner[0]][cleaner[1]] = -1

if __name__ == "__main__":
    # 입력 & 전처리
    R, C, T = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(R)]
    for i in range(R):
        if A[i][0] == -1:
            top_cleaner, btm_cleaner = [i,0], [i+1,0]
            break
    top_delta = [[0,1],[-1,0],[0,-1],[1,0]]
    btm_delta = [[0,1],[1,0],[0,-1],[-1,0]]
    
    for tc in range(T):
        A = dusting(R, C, A)
        air_cleaning(R, C, A, top_cleaner, top_delta)
        air_cleaning(R, C, A, btm_cleaner, btm_delta)

    sum_result = 0
    for r in range(R):
        sum_result += sum(A[r])

    print(sum_result+2)