import sys
input = sys.stdin.readline


def dfs(N: int, M: int, idx: int, lst: list = []):
    """ 조합 구하기(백트래킹)
    Args: 
        N (int) : 입력된 전체 수열의 길이
        M (int) : 그만하는 조건의 길이
        lst (list) : 탐색중인 수열
    """
    
    if len(lst) == M:
        res.append(tuple(sorted(lst)))
        return
    
    if idx >= N:
        return
    
    for i in range(idx, N):
        lst.append(arr[i])
        dfs(N, M, i, lst)
        lst.pop()


if __name__ == "__main__": # 비트마스킹 연습
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    res = []

    dfs(N, M, 0)

    result = list(set(res))
    result.sort()
    for r in result:
        print(*r)
