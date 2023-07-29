import sys
import collections
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def func(w: int) -> int:

    if not tree[w] or dp[w] != -1:
        if dp[w] == -1:
            dp[w] = time[w]
        return dp[w]
    
    v = 0
    for t in tree[w]:
        v = max(func(t), v)
    
    dp[w] = v + time[w]
    return dp[w]

if __name__ == "__main__":
    T =int(input())
    for tc in range(T):
        time =[0]
        tree = collections.defaultdict(list)
        N, K = map(int,input().split())
        dp = [-1] * (N+1)
        time.extend(list(map(int,input().split())))
        for k in range(K):
            x, y = map(int,input().split())
            tree[y].append(x)
        W = int(input())

        res = func(W)

        print(res)