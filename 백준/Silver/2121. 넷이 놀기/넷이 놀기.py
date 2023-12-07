import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    A, B = map(int, input().split())
    is_point = set()
    for n in range(N):
        x, y = map(int, input().split())
        is_point.add((x, y))

    res = 0
    for i, j in is_point:

        if not (i+A, j) in is_point:
            continue

        if not (i, j+B) in is_point:
            continue
        
        if not (i+A, j+B) in is_point:
            continue

        res += 1
    print(res)
