import sys
input = sys.stdin.readline

def solve(s: int, k: int, h: int) -> str:
    if sum([s, k, h]) >= 100:
        return 'OK'

    m = min(s, k, h)
    if m == s:
        return 'Soongsil'
    if m == k:
        return 'Korea'
    return 'Hanyang'


def main():
    # 입력값
    s,k,h = map(int, input().split())
    
    # 풀이
    result = solve(s, k, h)

    # 출력
    print(result)


if __name__ == "__main__":
    main()

