import sys
def solve(points: list[tuple[int,int]]) -> int:
    cols = {}
    for x,y in points:
        cols.setdefault(x, []).append(y)
    xs = sorted(cols)
    ys_lists = [sorted(cols[x]) for x in xs]
    ans = 0
    m = len(xs)
    for i in range(m):
        yi = ys_lists[i]
        for j in range(i+1, m):
            yj = ys_lists[j]
            a = b = cnt = 0
            ni, nj = len(yi), len(yj)
            while a < ni and b < nj:
                if yi[a] < yj[b]:
                    a += 1
                elif yi[a] > yj[b]:
                    b += 1
                else:
                    cnt += 1
                    a += 1
                    b += 1
            if cnt >= 2:
                ans += cnt*(cnt-1)//2
    return ans

def main():
    # 입력
    input = sys.stdin.readline
    N = int(input().strip())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    # 풀이
    result = solve(points)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
