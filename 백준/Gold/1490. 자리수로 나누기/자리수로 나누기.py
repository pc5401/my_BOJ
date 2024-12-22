import sys
input = sys.stdin.readline


def solve(N: str) -> int:
    lst = list({ int(i) for i in N if i != '0'})
    n = int(N)

    if all([ not n % x for x in lst]):
        return n

    cnt = 10
    m = 0
    n *= 10

    while any([n % x for x in lst]):
        m += 1

        if m == cnt:
            cnt *= 10
            n = int(N) * cnt
            m = 0
            continue

        n += 1

    return n


if __name__ == '__main__':
    # 입력값
    N = input().rstrip()
    result = solve(N)

    # 출력
    print(result)