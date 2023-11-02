import sys
import math
input = sys.stdin.readline

if __name__ == "__main__":
    N, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x : x[0])
    res = 0
    for i in range(N):
        a, b = data[i]
        if i > 0 and data[i-1][1] > a:
            a = data[i-1][1]
        l = b - a
        v = math.ceil(l/L)
        res += v
        data[i][1] = a + (v * L)
    print(res)