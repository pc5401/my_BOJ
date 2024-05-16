import sys
input = sys.stdin.readline


def solve(a: int, b: int) -> int:
    if (b % a != 0): return 0
    return (b//a) >= 2

def main():
    # 입력값
    Q: int = int(input())
    data = [tuple(map(int, input().split())) for _ in range(Q)]
    # 풀이
    result: list[int] = [ 1 if solve(a, b) else 0 for a, b in data]

    # 출력
    for res in result:
        print(res)
    

if __name__ == "__main__":
    main()
