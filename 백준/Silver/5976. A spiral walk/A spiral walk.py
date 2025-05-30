import sys
input = sys.stdin.readline

def solve(N: int) -> list[list[int]]:
    mat = [[0]*N for _ in range(N)]
    top, bottom, left, right = 0, N-1, 0, N-1
    num = 1
    while top <= bottom and left <= right:
        # 오른쪽으로
        for j in range(left, right+1):
            mat[top][j] = num
            num += 1
        top += 1
        # 아래로
        for i in range(top, bottom+1):
            mat[i][right] = num
            num += 1
        right -= 1
        if top <= bottom:
            # 왼쪽으로
            for j in range(right, left-1, -1):
                mat[bottom][j] = num
                num += 1
            bottom -= 1
        if left <= right:
            # 위로
            for i in range(bottom, top-1, -1):
                mat[i][left] = num
                num += 1
            left += 1
    return mat

def main():
    # 입력
    N = int(input())
    # 풀이
    mat = solve(N)
    # 출력
    for row in mat:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
