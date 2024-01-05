import sys
input = sys.stdin.readline

def gcm(n, m) -> int: # 최대공약수
    maxV = max(n, m)
    rtn = 1
    for i in range(1, maxV+1):
        if n % i or m % i:
            continue
        rtn = i

    return rtn

if __name__ == "__main__":
    N, M = map(int,input().split())
    g = gcm(N, M)
    print(g)
    print(N*M//g)