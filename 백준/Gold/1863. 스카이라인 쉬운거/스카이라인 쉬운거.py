import sys
input = sys.stdin.readline


if __name__ == '__main__':
    # 입력값
    N = int(input())
    sky_lines = [tuple(map(int, input().split())) for _ in range(N)]
    sky_lines.sort()
    res = 0
    stack = []

    for x, h in sky_lines:
        if not stack or stack[-1] < h:
            stack.append(h)
            continue

        while stack and stack[-1] > h:
            if stack.pop() > 0:
                res += 1
        if h and(not stack or stack[-1] < h):
            stack.append(h)
    res += len([h for h in stack if h > 0])
    print(res)

