import sys
input = sys.stdin.readline


def check(s: str, t: str) -> bool:
    l = min(len(s), len(t))

    for i in range(l):
        if s[-i-1:] == t[0:i+1]:
            return 1
        
        if t[-i-1:] == s[0:i+1]:
            return 1

    return 0


def solve(n:int, words: list[str]) -> int:
    rtn = 0

    for i in range(n-1):
        for j in range(i+1, n):
            rtn += check(words[i], words[j])
    
    return rtn


def main():
    n = int(input())
    words = [input().rstrip() for _ in range(n)]

    print(solve(n, words))


main()

