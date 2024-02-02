import sys
input = sys.stdin.readline


def solve_KMP(N: int, M: int, words: str) -> int:
    res = 0
    pattern = 'I' + 'OI' * N
    
    table = [0] * (2*N+1)
    j = 0 
    
    for i in range(1, (2*N+1)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    j = 0
    
    for i in range(M):
        while j > 0 and words[i] != pattern[j]:
            j = table[j-1]
        
        if words[i] == pattern[j]:
            if j == (2*N):
                res += 1
                j = table[j]
            else:
                j += 1

    return res


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    W = input().rstrip()
    print(solve_KMP(N, M, W))