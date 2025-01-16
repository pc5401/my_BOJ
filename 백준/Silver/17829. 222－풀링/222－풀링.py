import sys
input = sys.stdin.readline

def solve(N: int, matrix: list[int]):
    if N == 1:
        return matrix[0][0]
    newN = N // 2
    next_matrix = [[0]*newN for _ in range(newN)]
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            block = [ matrix[i][j], matrix[i][j+1],
                matrix[i+1][j], matrix[i+1][j+1] ]
            block.sort(reverse=True)
            next_matrix[i//2][j//2] = block[1]
    
    return solve(newN, next_matrix)


def main():
    # 입력
    N = int(input())
    metrix = [list(map(int, input().split())) for _ in range(N)]

    # 풀이
    result = solve(N, metrix)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
