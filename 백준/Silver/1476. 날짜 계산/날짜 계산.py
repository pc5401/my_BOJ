import sys
input = sys.stdin.readline


def solve(E: int, S: int, M: int) -> int:
    e, s, m = 1, 1 ,1
    year = 1

    while e != E or s != S or m != M:
        year += 1

        e = e+1 if e < 15 else 1
        s = s+1 if s < 28 else 1
        m = m+1 if m < 19 else 1

    return year


def main():
    # 입력
    E, S, M = map(int, input().split())
    # 풀이
    result = solve(E, S, M)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()