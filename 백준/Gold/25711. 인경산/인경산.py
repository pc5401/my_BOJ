import sys, math
input = sys.stdin.readline

def solve(N: int, Q: int, X: list[int], Y: list[int], queries: list[tuple[int, int]]) -> list[float]:
    forward = [0.0] * (N - 1)
    for i in range(N - 1):
        dx = X[i + 1] - X[i]
        dy = Y[i + 1] - Y[i]
        dist = math.sqrt(dx * dx + dy * dy)
        if Y[i + 1] > Y[i]:
            cost = 3 * dist
        elif Y[i + 1] == Y[i]:
            cost = 2 * dist
        else:
            cost = 1 * dist
        forward[i] = cost
        
    forward_prefix = [0.0] * N
    forward_prefix[0] = 0.0
    for i in range(1, N):
        forward_prefix[i] = forward_prefix[i - 1] + forward[i - 1]
    
    backward = [0.0] * N
    for i in range(1, N):
        dx = X[i] - X[i - 1]
        dy = Y[i] - Y[i - 1]
        dist = math.sqrt(dx * dx + dy * dy)
        if Y[i - 1] < Y[i]:
            cost = 1 * dist
        elif Y[i - 1] == Y[i]:
            cost = 2 * dist
        else:
            cost = 3 * dist
        backward[i] = cost
        
    backward_prefix = [0.0] * N
    backward_prefix[0] = 0.0
    for i in range(1, N):
        backward_prefix[i] = backward_prefix[i - 1] + backward[i]
    
    results = []
    for (i, j) in queries:
        start = i - 1
        end = j - 1
        if start <= end:
            cost = forward_prefix[end] - forward_prefix[start]
        else:
            cost = backward_prefix[start] - backward_prefix[end]
        results.append(cost)
    return results

def main():
    # 입력
    N, Q = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    queries = []
    for _ in range(Q):
        i, j = map(int, input().split())
        queries.append((i, j))
    
    # 풀이
    results = solve(N, Q, X, Y, queries)
    
    # 출력
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
