import sys
input = sys.stdin.readline

def solve(n: int, v: list[int]) -> int:
    need = 1
    for vi in reversed(v):
        # 최소 k*vi
        k = (need + vi - 1) // vi
        need = k * vi
    return need

def main():
    # 입력
    n = int(input().strip())
    v = list(map(int, input().split()))
    # 풀이
    result = solve(n, v)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
