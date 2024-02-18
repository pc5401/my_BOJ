import sys
input = sys.stdin.readline


def solve(m: int, lst: list) -> int:
    step = 0

    while lst:
        step += 2 * lst.pop()
        for _ in range(m-1):
            if lst: lst.pop()
            else: break

    return step


if __name__ == '__main__':
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    left = sorted([-p for p in lst if p < 0])
    right = sorted([p for p in lst if p > 0])
    
    if left and right:
        if left[-1] > right[-1]:
            remain = left.pop()
            for _ in range(M - 1): 
                if left:
                    left.pop()
        else:
            remain = right.pop()
            for _ in range(M - 1): 
                if right:
                    right.pop()

        print(solve(M, left) + solve(M, right) + remain)

    elif left:
        remain = left.pop()
        for _ in range(M - 1): 
            if left:
                left.pop()
        print(solve(M, left) + remain)

    elif right:
        remain = right.pop()
        for _ in range(M - 1): 
            if right:
                right.pop()
        print(solve(M, right) + remain)