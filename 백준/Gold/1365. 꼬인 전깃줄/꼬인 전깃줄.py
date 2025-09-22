import sys
from bisect import bisect_left
input = sys.stdin.readline

def solve(N, A):
    tails = []
    for x in A:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return N - len(tails)

def main():
    # 입력
    data = list(map(int, sys.stdin.buffer.read().split()))
    N = data[0]
    A = data[1:1+N]

    # 풀이
    result = solve(N, A)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
