import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int,input().split())
    S = [input().rstrip() for _ in range(N)]
    
    res_cnt = 0
    res_str = ''

    for words in zip(*S):
        A, T, G, C = 0, 0, 0, 0
        for word in words:
            if word == 'A':
                A += 1
            elif word == 'C':
                C += 1
            elif word == 'G':
                G += 1
            elif word == 'T':
                T += 1
        
        maxV = max(A, T, G, C)
        if maxV == A:
            res_str += 'A'
        elif maxV == C:
            res_str += 'C'
        elif maxV == G:
            res_str += 'G'
        elif maxV == T:
            res_str += 'T'
        
        res_cnt += (N - maxV)
    
    print(res_str)
    print(res_cnt)