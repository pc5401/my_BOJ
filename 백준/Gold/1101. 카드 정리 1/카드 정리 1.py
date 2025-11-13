import sys

def solve(N, M, boxes):
    cnt_nonzero = []
    pure_color = []
    for i in range(N):
        nz = [c for c in range(M) if boxes[i][c] > 0]
        cnt_nonzero.append(len(nz))
        pure_color.append(nz[0] if len(nz) == 1 else -1)

    ans = 10**9
    for j in range(N):  # joker box
        mixed = 0
        pure_count = [0] * M
        for i in range(N):
            if i == j:
                continue
            if cnt_nonzero[i] >= 2:
                mixed += 1
            elif cnt_nonzero[i] == 1:
                pure_count[pure_color[i]] += 1
        cost = mixed + sum(max(0, pc - 1) for pc in pure_count)
        if cost < ans:
            ans = cost
    return ans

def main():
    #입력
    input = sys.stdin.readline
    N, M = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(N)]
    #풀이
    res = solve(N, M, boxes)
    #출력
    print(res)

if __name__ == "__main__":
    main()
