def solution(citations):
    answer = 0
    ans = []
    n = len(citations)
    citations.sort()
    for h in range(n):
        cnt = 0
        for c in citations:
            if c > h:
                break
            cnt += 1
            
        if cnt >= h and h >= n - cnt:
            ans = h
    
    return ans