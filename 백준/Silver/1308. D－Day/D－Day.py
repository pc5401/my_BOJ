import sys
input = sys.stdin.readline

def count_days(date: list[int]) -> int:
    y, m, d = date
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    cnt = y * 365 + sum([months[i] for i in range(m)]) + d

    cnt += ((y-1) // 4)
    cnt -= ((y-1) // 100)
    cnt += ((y-1) // 400)

    if y % 4 == 0 and (not y % 100 == 0 or  y % 400 == 0):
        if m > 2:
            cnt += 1

    return cnt


def solve(t: list[int], d: list[int]) -> int:
    if d[0] - t[0] > 1000:
        return 'gg'

    if d[0] - t[0] == 1000:
        if d[1] > t[1]:
            return 'gg'
        elif d[1] == t[1] and d[2] >= t[2]:
            return 'gg'
        
    return f'D-{count_days(d) - count_days(t)}'

if __name__ == "__main__":
    today = list(map(int, input().split()))
    d_day = list(map(int, input().split()))


    result = solve(today, d_day)

    print(result)
