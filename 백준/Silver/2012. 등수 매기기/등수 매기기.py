import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    data = [int(input()) for _ in range(N)]
    data.sort()
    res = 0
    for i in range(N):
        res += abs(data[i]-i-1)
    print(res)
