import sys
import collections
input = sys.stdin.readline

def dp_setting(n:int):
    dp = [0 for _ in range(n+1)]
    dct = collections.defaultdict(list)
    for i in range(1,n+1):
        v = list(map(int,input().split()))
        dp[i] = v[0]
        dct[i] = v[1:] 
        if dct[i][0] == -1: # 딕셔너리에 체크 만약 첫 값이 -1 이면 끝
            visit[i] = 1

    return dp, dct

# dfs 로 풀이, 방문지 중복 안 되게 체크
def dfs_solve(n:int) -> int:
    global dp, dct

    if visit[n]:
        return dp[n]
    
    lst = []
    for v in dct[n]:
        if v == -1:
            break
        lst.append(dfs_solve(v))

    dp[n] += max(lst)
    visit[n] = 1
    return dp[n]


if __name__ == "__main__":
    N = int(input())
    visit = [0] * (N+1)
    dp, dct = dp_setting(N)
    for num in range(1,N+1):
        print(dfs_solve(num))