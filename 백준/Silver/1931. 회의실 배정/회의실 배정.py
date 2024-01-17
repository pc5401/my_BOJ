import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    I = [ tuple(map(int, input().split())) for _ in range(N) ]
    I.sort(key=lambda x : (x[1], x[0]))

    cnt = 0
    t = 0

    for i in I:
        if i[0] >=t:
            cnt += 1
            t = i[1]
    
    print(cnt)