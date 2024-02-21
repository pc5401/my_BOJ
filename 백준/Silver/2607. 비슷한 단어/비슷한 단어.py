import sys
import collections
input = sys.stdin.readline


def comparing(target: list, word: list, A: dict) -> bool:
    n, m = len(target), len(word)
    B = [0] * 26
    
    for w in word: 
        B[ord(w) - 65] += 1
    
    for key, item in A.items():
        B[ord(key) - 65] -= item

    zero_cnt = B.count(0)
    x, y = B.count(1), B.count(-1)

    if n == m and zero_cnt == 26:
        return True
    elif n == m and zero_cnt == 24 and x == 1 and y == 1:
        return True
    elif n+1 == m and zero_cnt == 25 and x == 1:
        return True
    elif n == m+1 and zero_cnt == 25 and y == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    N = int(input())
    target =list(input().rstrip())
    lst = [list(input().rstrip()) for _ in range(N-1)]
    A = collections.Counter(target)
    
    res = 0
    for word in lst:
        if comparing(target, word, A):
            res += 1
    
    print(res)