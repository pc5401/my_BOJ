import sys
from collections import deque
input = sys.stdin.readline

def solve(F: int, S: int, G: int, U: int, D: int) -> int:
    Q = deque([(S, 0)])

    visited = [0] * (F+1)
    visited[0], visited[S] = 1, 1

    while Q:
        now, cnt = Q.popleft()

        if now == G:
            return cnt

        if now + U <= F and not visited[now + U]:
            visited[now + U] = 1
            Q.append((now+U, cnt+1))
        
        if now - D > 0 and not visited[now - D]:
            visited[now - D] = 1
            Q.append((now-D, cnt+1))


    return 'use the stairs'


    
def main():
    # 입력값
    F, S, G, U, D = map(int, input().split())

    # 풀이
    result = solve(F, S, G, U, D)

    # 결과 출력
    print(result)
        
if __name__ == '__main__':
    main()