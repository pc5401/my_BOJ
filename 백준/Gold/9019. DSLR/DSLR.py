# 시간 초과를 계속 해결 못 해서 chatGPT에게 도움 받은 코드

from collections import deque

# 함수는 딱 계산만한다 문자열은 따로 처리
def D(n):
    return (n * 2) % 10000

def S(n):
    return 9999 if n == 0 else n - 1

def L(n):
    return (n % 1000) * 10 + n // 1000

def R(n):
    return (n % 10) * 1000 + n // 10

def bfs(A, B):
    # set 대신에 list로 접근하도록 구성
    visited = [False] * 10000
    visited[A] = True
    Q = deque([(A, "")])

    while Q:
        n, s = Q.popleft()

        if n == B:
            return s

        for next_n, cmd in [(D(n), 'D'), (S(n), 'S'), (L(n), 'L'), (R(n), 'R')]:
            if not visited[next_n]:
                visited[next_n] = True
                Q.append((next_n, s + cmd))

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))