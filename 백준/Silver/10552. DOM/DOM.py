import sys
input = sys.stdin.readline

def solve(N: int, M: int, P: int, fav: list[int], hate: list[int]) -> int:
    next_channel = [0] * (M + 1)
    for a, b in zip(fav, hate):
        if next_channel[b] == 0:
            next_channel[b] = a

    visited = [False] * (M + 1)
    current = P
    steps = 0
    while next_channel[current] != 0:
        if visited[current]:
            return -1
        visited[current] = True
        current = next_channel[current]
        steps += 1
    return steps

def main():
    # 입력
    N, M, P = map(int, input().split())
    fav = []
    hate = []
    for _ in range(N):
        a, b = map(int, input().split())
        fav.append(a)
        hate.append(b)
    # 풀이
    result = solve(N, M, P, fav, hate)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
