import sys
input = sys.stdin.readline


def solve(N: int, A: list[int]) -> int:
    now, cnt = 0, 0
    visited = [0] * N

    while not visited[now]:
        if now == N-1:
            return cnt
        
        visited[now] = 1
        cnt += 1
        now = A[now]

    return 0

    
def main():
    # 입력값
    data = []
    T = int(input())
    for t in range(T):
        N = int(input())
        A = [int(input()) - 1 for _ in range(N)]
        data.append((N, A))

    # 풀이
    result = [solve(n, a) for n, a in data]
    
    # 결과 출력
    for res in result:
        print(res)
      
    
if __name__ == '__main__':
    main()