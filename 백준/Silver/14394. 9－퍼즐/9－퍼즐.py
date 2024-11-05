import sys
import collections
input = sys.stdin.readline

def solve(A: str, B: str) -> int:
    rtn = 0
    a = collections.Counter(*A)
    b = collections.Counter(*B)
    left = 0
    
    for w in 'RGBY':
        if w in b and w in a:
            rtn += (b[w] - a[w]) if b[w] - a[w] > 0 else 0
        elif w in b:
            rtn += b[w]
    
    return rtn

if __name__ == "__main__":
    # 입력값
    A = input().rsplit()
    B = input().rsplit()

    # 풀이
    result = solve(A, B)
    
    # 출력
    print(result)

