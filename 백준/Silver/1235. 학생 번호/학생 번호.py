import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input()) # 500_000_000_000 
    lst = [ input().replace("\n", "") for i in range(N)]
    res = 1
    while True:
        arr = {l[-res:] for l in lst}
        if len(arr) == N:
            break
        res += 1
    print(res)