import sys
input = sys.stdin.readline

def solve(n: int, d: int) -> int:
    cnt = 0
    sd = str(d)
    for i in range(1, n + 1):
        cnt += str(i).count(sd)
    return cnt

def main():
    # 입력
    n, d = map(int, input().split())
    # 풀이
    result = solve(n, d)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
