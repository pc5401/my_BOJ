import sys
input = sys.stdin.readline

def solve(X, K):
    y = 0
    p = 0
    while K > 0:
        if ((X >> p) & 1) == 0:
            if K & 1:
                y |= (1 << p)
            K >>= 1
        p += 1
    return y

def main():
    # 입력
    X, K = map(int, input().split())

    # 풀이
    result = solve(X, K)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
