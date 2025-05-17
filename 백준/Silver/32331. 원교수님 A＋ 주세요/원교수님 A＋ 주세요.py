import sys
input = sys.stdin.readline

def solve(N: int, M: int, X: int, Y: int, han_mid: int, others: list[tuple[str,int]]) -> tuple[bool,int]:

    totals = []
    for sid, mid in others:
        if sid.startswith("2024"):
            pred = Y + mid - X
            if pred < 0:
                pred = 0
            totals.append(mid + pred)
    totals.sort(reverse=True)

    if len(totals) >= M:
        threshold = totals[M-1]
    else:
        threshold = -10**30  
    need = threshold - han_mid
    F = max(0, need)
    if F <= Y:
        return True, F
    else:
        return False, -1

def main():
    # 입력
    N, M, X, Y = map(int, input().split())
    han_id, han_mid = input().split()
    han_mid = int(han_mid)
    others = [tuple(input().split()) for _ in range(N-1)]
    others = [(sid, int(mid)) for sid, mid in others]
    # 풀이
    ok, F = solve(N, M, X, Y, han_mid, others)
    # 출력
    if ok:
        print("YES")
        print(F)
    else:
        print("NO")

if __name__ == "__main__":
    main()
