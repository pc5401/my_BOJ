import sys

def cw_dist(a, b, n):
    return (a - b) % n

def ccw_dist(a, b, n):
    return (b - a) % n

def solve(cases):
    res = []
    for n, t1, t2, t3 in cases:
        ans = 4 * n - 1 + ccw_dist(t1, t2, n) + cw_dist(t2, t3, n)
        res.append(ans)
    return res

def main():
    #입력
    lines = sys.stdin.read().strip().splitlines()
    cases = []
    for line in lines:
        if not line.strip():
            continue
        n, t1, t2, t3 = map(int, line.split())
        if n == 0 and t1 == 0 and t2 == 0 and t3 == 0:
            break
        cases.append((n, t1, t2, t3))
    #풀이
    ans_list = solve(cases)
    #출력
    print("\n".join(map(str, ans_list)))

if __name__ == "__main__":
    main()
