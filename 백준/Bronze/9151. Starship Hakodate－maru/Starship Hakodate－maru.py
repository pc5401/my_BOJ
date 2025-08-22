import sys
input = sys.stdin.readline

MAXV = 151200

def build_best():
    cubes = []
    i = 0
    while True:
        v = i * i * i
        if v > MAXV:
            break
        cubes.append(v)
        i += 1

    tetras = []
    i = 0
    while True:
        v = i * (i + 1) * (i + 2) // 6
        if v > MAXV:
            break
        tetras.append(v)
        i += 1

    can = [False] * (MAXV + 1)
    for c in cubes:
        for t in tetras:
            s = c + t
            if s > MAXV:
                break
            can[s] = True

    best = [0] * (MAXV + 1)
    cur = 0
    for x in range(MAXV + 1):
        if can[x]:
            cur = x
        best[x] = cur
    return best

BEST = build_best()

def solve(n):
    return BEST[n]

def main():
    # 입력
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        # 풀이
        result = solve(n)
        # 출력
        out.append(str(result))
    print("\n".join(out))

if __name__ == "__main__":
    main()
