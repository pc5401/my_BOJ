import sys
input = sys.stdin.readline

def solve(N: int, mat: list[list[int]]) -> list[int]:
    for i in range(N):
        if mat[i][i] != 0:
            return [-1]
    for i in range(N):
        for j in range(N):
            if i != j:
                if mat[i][j] not in (-1, 1):
                    return [-1]
                if mat[i][j] != -mat[j][i]:
                    return [-1]
    result = [0] * N
    used = set()
    for i in range(N):
        s = sum(mat[i])
        if (N - s + 1) % 2 != 0:
            return [-1]
        r = (N - s + 1) // 2
        if r < 1 or r > N or r in used:
            return [-1]
        used.add(r)
        result[i] = r
    return result

def main():
    # 입력
    N = int(input().strip())
    mat = [list(map(int, input().split())) for _ in range(N)]
    
    # 풀이
    result = solve(N, mat)
    
    # 출력
    if result == [-1]:
        print(-1)
    else:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
