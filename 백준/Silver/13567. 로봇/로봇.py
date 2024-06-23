import sys
input = sys.stdin.readline


def solve(M: int, order_list: list[list[str]]) -> int:
    x, y, dir = 0, 0, 0
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for order, i in order_list:
        if order == 'TURN':
            if i == '1':
                dir = dir - 1 if dir > 0 else 3
            else:
                dir = (dir + 1) % 4
        
        else: # MOVE
            n = int(i)
            nx = x + (delta[dir][0] * n)
            ny = y + (delta[dir][1] * n)
            
            if 0 <= nx < M and 0 <= ny < M:
                x = nx
                y = ny
            
            else:
                return (-1,)

    return x, y


def main():
    # 입력값
    M, n = map(int, input().split())
    order_list: list[list[str]] = [input().split() for _ in range(n)]

    # 풀이
    result: tuple[int, int] = solve(M, order_list)

    # 출력
    print(*result)


if __name__ == "__main__":
    main()
