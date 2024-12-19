import sys
input = sys.stdin.readline

def solve(N, M, matrix):
    max_sum = -10_000 * N * M 

    for left in range(M):
        value = [0] * N
        for right in range(left, M):
            for i in range(N):
                value[i] += matrix[i][right]

            now_sum = 0
            for val in value:
                now_sum += val
                if now_sum > max_sum:
                    max_sum = now_sum
                if now_sum < 0:
                    now_sum = 0
    return max_sum

if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = solve(N, M, matrix)
    print(result)
