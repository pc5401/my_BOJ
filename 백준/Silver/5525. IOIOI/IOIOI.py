import sys
input = sys.stdin.readline


def create_word(N):
    rtn = 'I'
    for _ in range(N):
        rtn += 'OI'
    return rtn

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    S = input().rstrip()
    
    W = create_word(N)
    res = 0

    for i in range(M - (2*N+1)+1):
        if S[i] == 'I' and S[i:i+2*N+1:1] == W:
            res += 1
    
    print(res)
