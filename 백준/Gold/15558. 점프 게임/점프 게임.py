import sys
from collections import deque
input = sys.stdin.readline


def solve(N, k, A, B):
    visited = [[False] * N for _ in range(2)]
    
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0] = True

    while queue:
        line, pos, t = queue.popleft()

        if pos >= N:
            return 1

        next_pos = pos + 1
        if next_pos >= N:  
            return 1 
        if next_pos > t and not visited[line][next_pos] and (
            (line == 0 and A[next_pos] == 1) or (line == 1 and B[next_pos] == 1)
        ):
            visited[line][next_pos] = True
            queue.append((line, next_pos, t + 1))

        next_pos = pos - 1
        if next_pos >= 0:
            if next_pos > t and not visited[line][next_pos] and (
                (line == 0 and A[next_pos] == 1) or (line == 1 and B[next_pos] == 1)
            ):
                visited[line][next_pos] = True
                queue.append((line, next_pos, t + 1))

        next_pos = pos + k
        next_line = 1 - line
        if next_pos >= N:
            return 1
        if next_pos > t and not visited[next_line][next_pos] and (
            (next_line == 0 and A[next_pos] == 1) or (next_line == 1 and B[next_pos] == 1)
        ):
            visited[next_line][next_pos] = True
            queue.append((next_line, next_pos, t + 1))

    return 0



if __name__ == '__main__':
    # 입력값
    N, k = map(int, input().split())
    A = list(map(int, list(input().rstrip())))
    B = list(map(int, list(input().rstrip())))
    
    result = solve(N, k, A, B)

    print(result)