import sys
input = sys.stdin.readline

def solve(n, m, elevators):
    from math import gcd

    mina = float('inf')
    for u, d in elevators:
        g = gcd(u, d)
        uc = d // g      # lcm / u
        dc = u // g      # lcm / d
        cycle = uc + dc

        rem = n % cycle
        if rem == 0:
            rem = cycle

        floor = 0
        for _ in range(rem):
            if floor - d <= 0:
                floor += u
            else:
                floor -= d

        if floor < mina:
            mina = floor

    return mina

def main():
    # 입력
    n, m = map(int, input().split())
    elevators = [tuple(map(int, input().split())) for _ in range(m)]

    # 풀이
    result = solve(n, m, elevators)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
