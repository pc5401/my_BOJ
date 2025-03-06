import sys
input = sys.stdin.readline

def solve(M: int, segs: list[tuple[int, int]]) -> int:
    segs.sort(key=lambda x: (x[0], -x[1]))
    cur = 0
    cnt = 0
    i = 0
    n = len(segs)
    while cur < M:
        best = cur
        while i < n and segs[i][0] <= cur:
            if segs[i][1] > best:
                best = segs[i][1]
            i += 1
        if best == cur:
            return 0
        cnt += 1
        cur = best
    return cnt

def main():
    # 입력
    M_line = input().strip()
    while M_line == "":
        M_line = input().strip()
    M = int(M_line)
    segs = []
    while True:
        line = input().strip()
        if not line:
            continue
        L, R = map(int, line.split())
        if L == 0 and R == 0:
            break
        segs.append((L, R))
    
    # 풀이
    result = solve(M, segs)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
