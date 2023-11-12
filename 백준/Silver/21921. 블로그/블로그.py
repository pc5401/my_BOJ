import sys
input = sys.stdin.readline


def stack_sum(N, visited):
    lst = [0] * (N+1)
    for i in range(N):
        lst[i+1] = lst[i] + visited[i]

    return lst

if __name__ == "__main__":
    N, X = map(int, input().split())
    visited = list(map(int, input().split()))
    stack_data = stack_sum(N, visited)
    ans = 0
    cnt = 0
    for i in range(N-X+1):
        val = stack_data[X+i] - stack_data[i]
        if val > ans:

            ans = stack_data[X+i] - stack_data[i]
            cnt = 1
        elif val == ans:
            cnt += 1

    if ans:
        print(ans)
        print(cnt)
    else:
        print('SAD')