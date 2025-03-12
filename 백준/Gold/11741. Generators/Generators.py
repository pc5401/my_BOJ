import sys
input = sys.stdin.readline

def solve(n: int, k: int, params: list[tuple[int, int, int, int]]) -> tuple[int, list[int]]:
    max_val_list = [0] * n
    t_max_list = [0] * n
    cand_delta_list = [None] * n 
    t_cand_list = [None] * n

    for j in range(n):
        x0, a, b, c = params[j]
        seen = {}
        values = {}
        t = 0
        x = x0
        while x not in seen:
            seen[x] = t
            if x not in values:
                values[x] = t
            t += 1
            x = (a * x + b) % c
        
        all_vals = list(values.keys())
        M = max(all_vals)
        tM = values[M]
        second = -1
        t_second = None
        for v in all_vals:
            if v < M and v > second:
                second = v
                t_second = values[v]
        max_val_list[j] = M
        t_max_list[j] = tM
        if second != -1:
            cand_delta_list[j] = M - second
            t_cand_list[j] = t_second
        else:
            cand_delta_list[j] = None
            t_cand_list[j] = None

    S = sum(max_val_list)
    chosen = t_max_list[:]

    if S % k != 0:
        return S, chosen

    best_delta = None
    best_j = -1
    for j in range(n):
        delta = cand_delta_list[j]
        if delta is None:
            continue
        if delta % k == 0:
            continue
        if best_delta is None or delta < best_delta:
            best_delta = delta
            best_j = j

    if best_delta is None:
        return -1, []
    S -= best_delta
    chosen[best_j] = t_cand_list[best_j]
    return S, chosen

def main():
    # 입력
    line = input().split()
    n = int(line[0])
    k = int(line[1])
    params = []
    for _ in range(n):
        x0, a, b, c = map(int, input().split())
        params.append((x0, a, b, c))
    
    # 풀이
    total, ts = solve(n, k, params)
    if total == -1:
        print(-1)
    else:
        print(total)
        print(" ".join(map(str, ts)))

if __name__ == "__main__":
    main()
