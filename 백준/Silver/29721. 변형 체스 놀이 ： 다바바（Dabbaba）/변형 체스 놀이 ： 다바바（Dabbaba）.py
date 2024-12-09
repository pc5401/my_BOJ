import sys
input = sys.stdin.readline

def solve(n: int, k: int, lst: list[int]) -> int:
    visited = set()

    for x, y in lst:
        visited.add((x - 1, y - 1))

    cnt = 0

    for x, y in lst:
        for d in [[0,-2], [-2, 0], [0, 2], [2, 0]]:
            ni = x + d[0] - 1
            nj = y + d[1] - 1 
            if 0 <= ni < n and 0 <= nj < n and not (ni, nj) in visited:
                visited.add((ni, nj))
                cnt += 1
    
    return cnt

    
def main():
    # 입력값
    N, K = map(int, input().split())
    lst = [tuple(map(int, input().split())) for _ in range(K)]

    # 풀이
    result = solve(N, K, lst)
    
    # 결과 출력
    print(result)
        
if __name__ == '__main__':
    main()