import collections
import sys
input = sys.stdin.readline


def solve(W: list, K: int) -> tuple:
    minV, maxV = float('INF'), 0
    if K == 1:
        return 1, 1

    word_lst = collections.defaultdict(list)
    for i, w in enumerate(W):
        word_lst[w].append(i)

    for word in word_lst:
        n = len(word_lst[word])
        if n < K:
            continue
        for i in range(n-K+1):
            value = word_lst[word][i+K-1] - word_lst[word][i] + 1
            minV = min(minV, value)
            maxV = max(maxV, value)
    
    return minV, maxV



if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        W = list(input().rstrip())
        K = int(input())
        res = solve(W, K)
        
        if res[0] == float('INF') or res[1] == 0:
            print(-1)
        else:
            print(*res)
