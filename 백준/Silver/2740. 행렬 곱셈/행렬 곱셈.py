import sys
input = sys.stdin.readline


def solve(N: int, M: int, K: int, A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    rtn = []

    for a in A:
        lst = [sum([a[j]* B[j][i] for j in range(M)]) for i in range(K)]
        rtn.append(lst)
    return rtn


def main():
    # 입력값
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    M, K = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(M)]
    
    # 풀이
    result = solve(N, M, K, A, B)
    
    # 출력
    for res in result:
        print(*res)

if __name__ == "__main__":
    main()
