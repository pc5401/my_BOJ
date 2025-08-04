import sys
input = sys.stdin.readline

def solve(N, L, lights):
    time = 0
    prev = 0
    for D, R, G in lights:
        time += D - prev
        cycle = R + G
        rem = time % cycle

        if rem < R:
            time += R - rem
        prev = D

    time += L - prev
    return time

def main():
    # 입력
    N, L = map(int, input().split())
    lights = [tuple(map(int, input().split())) for _ in range(N)]

    # 풀이
    result = solve(N, L, lights)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
