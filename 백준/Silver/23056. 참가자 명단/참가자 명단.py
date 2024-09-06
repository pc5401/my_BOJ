import sys
input = sys.stdin.readline


def solve(N: int, M: int, class_name: list[tuple[int, str]]) -> list[tuple[int, str]]:
    blue = []
    white = []

    limited = { i:0 for i in range(1, N+1) }

    for cls, name in class_name:
        limited[cls] += 1
        if limited[cls] > M:
            continue
        
        if cls % 2:
            blue.append((cls, name))
        else:
            white.append((cls, name))
    
    blue.sort(key=lambda x : (x[0], len(x[1]), x[1]))
    white.sort(key=lambda x : (x[0], len(x[1]), x[1]))

    return blue + white


def main():
    # 입력값
    N, M = map(int, input().split())
    class_name = []
    while True:
        a, b = input().split()
        if a == '0' and b == '0':
            break
        class_name.append((int(a), b))

    # 풀이
    result = solve(N, M, class_name)

    # 출력
    for res in result:
        print(*res)


if __name__ == "__main__":
    main()


