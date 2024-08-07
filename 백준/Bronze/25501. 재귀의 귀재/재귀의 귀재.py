import sys
input = sys.stdin.readline


def solve(S: str):
    cnt = 0

    def recursion(s, l, r):
        nonlocal cnt
        cnt += 1
        if l >= r: return 1
        elif s[l] != s[r]: return 0
        else: return recursion(s, l+1, r-1)

    def isPalindrome(s):
        return recursion(s, 0, len(s)-1)
    
    return isPalindrome(S), cnt

def main():
    T = int(input())
    lst = [input().rstrip() for _ in range(T)]
    result = [solve(lst[i]) for i in range(T)]
    for res in result:
        print(*res)

main()

