import sys
input = sys.stdin.readline

def solve(H: int, W: int, world: list[str]) -> list[int]:
    rtn = [[-1] * W for _ in range(H)]

    for i in range(H): # 초기화
        for j in range(W):
            if world[i][j] == 'c':
                rtn[i][j] = 0
    
    for i in range(H):
        for j in range(1, W):
            if rtn[i][j - 1] >= 0 and rtn[i][j] == -1:
                rtn[i][j] = rtn[i][j - 1] + 1

    return rtn
    

if __name__ == "__main__":
    H, W  = map(int, input().split())
    world = [input().rstrip() for _ in range(H)]
    
    # 풀이
    result = solve(H, W, world)
    
    # 출력
    for res in result:
        print(*res)
