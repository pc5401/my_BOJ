import sys
input = sys.stdin.readline

def solve(n: int, files: list[str], m: int, intervals: list[tuple[int, int]]) -> list[str]:
    ans = []
    for l, r in intervals:
        for i in range(l - 1, r):
            ans.append(files[i])
    return ans

def main():
    # 입력
    n = int(input().strip())
    files = [input().rstrip('\n') for _ in range(n)]
    m = int(input().strip())
    intervals = []
    for _ in range(m):
        l, r = map(int, input().split())
        intervals.append((l, r))
    
    # 풀이
    ans = solve(n, files, m, intervals)
    
    # 출력
    print("\n".join(ans))

if __name__ == "__main__":
    main()
