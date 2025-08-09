import sys
from itertools import permutations
input = sys.stdin.readline

def min_period(s: str) -> int:
    L = len(s)
    pi = [0] * L
    for i in range(1, L):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    p = L - pi[-1]
    return p if L % p == 0 else L

def solve(N, words, K):
    L = sum(len(w) for w in words)
    if K == 0 or K > L or L % K != 0:
        return 0
    ans = 0
    for perm in permutations(range(N)):
        T = ''.join(words[i] for i in perm)
        p = min_period(T)
        if L // p == K:
            ans += 1
    return ans

def main():
    # 입력
    N = int(input().strip())
    words = [input().strip() for _ in range(N)]
    K = int(input().strip())

    # 풀이
    result = solve(N, words, K)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
