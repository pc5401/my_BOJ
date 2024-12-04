import sys
from collections import deque
input = sys.stdin.readline

def solve(N: int, S: int, A: list[int]) -> int:
    rtn = 0
    vistied = [0] * N

    Q = deque()
    Q.append(S)
    vistied[S] = 1

    while Q:
        node = Q.popleft()
        rtn += 1

        up = node + A[node]
        down = node - A[node]

        if up < N and not vistied[up]:
            vistied[up] = 1
            Q.append(up)
        
        if down >= 0 and not vistied[down]:
            vistied[down] = 1
            Q.append(down)

    return rtn

    
def main():
    # 입력값
    N = int(input())
    A = list(map(int, input().split()))
    S = int(input())

    # 풀이
    result = solve(N, S-1, A)
    
    # 결과 출력
    print(result)
        
if __name__ == '__main__':
    main()