import sys
input = sys.stdin.readline

def solve(N: int, freq: list[int], total: int, total2: int) -> tuple[int,int]:
    # 중앙값
    pos = (N - 1) // 2
    cum = 0
    for v, c in enumerate(freq):
        cum += c
        if cum > pos:
            rep1 = v
            break
    
    # 평균 근처
    m1 = total // N
    candidates = [m1]
    if total % N != 0:
        candidates.append(m1 + 1)
    best = None
    best_x = None
    
    for x in candidates:
        val = total2 - 2 * x * total + N * x * x
        if best is None or val < best or (val == best and x < best_x):
            best = val
            best_x = x
    return rep1, best_x

def main():
    # 입력
    N = int(input().strip())
    data = sys.stdin.read().split()
    total = 0
    total2 = 0
    freq = [0] * 10001
    for x in map(int, data):
        freq[x] += 1
        total += x
        total2 += x * x
    # 풀이
    r1, r2 = solve(N, freq, total, total2)
    # 출력
    print(r1, r2)

if __name__ == "__main__":
    main()
