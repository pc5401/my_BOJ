import sys
input = sys.stdin.readline


if __name__ == "__main__":
    A, B = map(int, input().split())
    Q = [(B, 0)]
    res = -1

    while Q:
        b, cnt = Q.pop()

        if b == A:
            res = cnt+1
            break
        
        if b and b % 2 == 0:
            Q.append((b // 2, cnt+1))

        if b % 10 == 1:
            Q.append((b // 10, cnt+1))


    print(res)
