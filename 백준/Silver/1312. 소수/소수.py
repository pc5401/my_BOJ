import sys
input = sys.stdin.readline


def main():
    A, B, N = map(int,input().split())
    
    x = A % B
    res = 0
    for _ in range(N):
        x *= 10
        if x // B:
            res = x // B
            x = x % B
        else:
            res = 0
    print(res)



if __name__ == "__main__":
    main()
