import sys
import itertools
input = sys.stdin.readline

def solve(A_team:tuple):
    global res

    A = 0
    for i in A_team:
        for j in A_team:
            A += arr[i][j]
    
    B = 0
    B_team = [i for i in range(N) if not i in A_team]
    for i in B_team:
        for j in B_team:
            B += arr[i][j]

    res = min(res, abs(A - B))

if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    c = N // 2 # 한 팀의 인원 수
    all_sum = sum([sum(arr[i]) for i in range(N)])
    res = 1e9
    for comb in map(solve, itertools.combinations(range(N), c)):
        pass
    print(res)