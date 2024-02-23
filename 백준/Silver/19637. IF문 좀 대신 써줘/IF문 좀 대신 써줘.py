import sys
import bisect
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().split())
    data = [input().split() for _ in range(N)]
    characters = [int(input()) for _ in range(M)]

    titles = [data[i][0] for i in range(N)]
    conditions = [int(data[i][1]) for i in range(N)]
    
    res = []
    
    for power in characters:
        i = bisect.bisect_left(conditions, power,hi=N-1)
        res.append(titles[i])

    for r in res:
        print(r)