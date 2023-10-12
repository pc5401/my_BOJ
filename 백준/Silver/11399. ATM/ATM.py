import sys
input = sys.stdin.readline

if __name__ == "__main__":
    # 입력 & 전처리
    N = int(input())
    P = list(map(int, input().split()))
    P.sort()
    res = 0
    time = 0
    for i in range(N):
        time += P[i]
        res += time
    print(res)