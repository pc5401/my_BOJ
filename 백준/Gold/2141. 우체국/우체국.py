import sys
input = sys.stdin.readline

def solve(N, XA):
    XA.sort(key=lambda t: t[0])
    total = sum(a for _, a in XA)
    half = (total + 1) // 2
    acc = 0
    for x, a in XA:
        acc += a
        if acc >= half:
            return x

def main():
    # 입력
    N = int(input().strip())
    XA = [tuple(map(int, input().split())) for _ in range(N)]

    # 풀이
    result = solve(N, XA)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
