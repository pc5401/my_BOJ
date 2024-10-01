def solve(s: str) -> str:
    n = len(s)
    z = s.count('0')
    o = s.count('1')
    z1 = 0
    for i in range(n):
        if s[i] == '0' and s[(i + 1) % n] == '1':
            z1 += 1
    p_shoot = z1 / z
    p_rotate = o / n
    if p_shoot < p_rotate:
        return "SHOOT"
    elif p_shoot > p_rotate:
        return "ROTATE"
    else:
        return "EQUAL"

def main():
    import sys
    s = sys.stdin.read().strip()
    print(solve(s))

if __name__ == "__main__":
    main()
