import sys
input = sys.stdin.readline


if __name__ == "__main__":
    T = int(input())
    res = []
    for _ in range(T):
        N = int(input())
        noob = [ tuple(map(int, input().split())) for _ in range(N) ]
        noob.sort()
        point = noob[0][1]
        res = 0
        
        for doc, spk in noob:
            if point >= spk:
                res += 1
                point =spk

        print(res)