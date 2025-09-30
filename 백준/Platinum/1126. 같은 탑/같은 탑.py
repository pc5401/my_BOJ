import sys
input = sys.stdin.readline

def solve(N, arr):
    dp = {0: 0}
    for h in arr:
        add = {}
        for d, t in dp.items():
            nd = d + h
            nv = t + h
            if add.get(nd, -1) < nv:
                add[nd] = nv
            if h <= d:
                nd = d - h
                nv = t
                if add.get(nd, -1) < nv:
                    add[nd] = nv
            else:
                nd = h - d
                nv = t - d + h
                if add.get(nd, -1) < nv:
                    add[nd] = nv
        for k, v in add.items():
            if dp.get(k, -1) < v:
                dp[k] = v
    ans = dp.get(0, 0)
    return ans if ans > 0 else -1

def main():
    # 입력
    N = int(input().strip())
    arr = list(map(int, input().split()))

    # 풀이
    result = solve(N, arr)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
