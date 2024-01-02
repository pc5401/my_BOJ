import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int,input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    res = 0
    for a in A:
        if not a in B:
            res += 1
    
    for b in B:
        if not b in A:
            res += 1

    print(res)
