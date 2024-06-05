import sys
input = sys.stdin.readline


def solve(N: int, SNS: list[list[int]]) -> list[int]:
    rtn = []
    while True:
        go_to = set()

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if i == j or i == k or j == k:
                        continue
                    
                    if SNS[i][j] == 0 and (SNS[i][k] and SNS[k][j]):
                        go_to.add((max(i,j), min(i,j)))

        cnt = len(go_to)
        if not cnt:
            return rtn
        rtn.append(cnt)

        for i, j in go_to:
            SNS[i][j] = 1
            SNS[j][i] = 1
        

def main():
    # 입력값
    N, M = map(int, input().split())
    SNS: list[list[int]] = [[0]*N for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        SNS[A-1][B-1] = 1
        SNS[B-1][A-1] = 1
    for i in range(N):
        SNS[i][i] = 1


    # 풀이
    result: list[int] = solve(N, SNS)
    # 출력
    print(len(result))
    for res in result:
        print(res)


if __name__ == "__main__":
    main()
