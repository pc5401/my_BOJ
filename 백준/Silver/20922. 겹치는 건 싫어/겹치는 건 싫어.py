import sys
import collections
input = sys.stdin.readline

def longest_continuous_subsequence(n: int,k: int, lst: list)-> int:
    lo, hi = 0, 0
    cnt = collections.defaultdict(int)
    cnt[lst[lo]] = 1
    rtn = 1
    
    for hi in range(1, n):
        cnt[lst[hi]] += 1

        if cnt[lst[hi]] > k:
            while lo < hi and cnt[lst[hi]] > k:
                cnt[lst[lo]] -= 1
                lo += 1
        
        rtn = max(rtn, hi - lo + 1)

    
    return rtn

if __name__ == '__main__':
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    print(longest_continuous_subsequence(N, K, lst))