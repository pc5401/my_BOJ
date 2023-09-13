import sys
import collections
input = sys.stdin.readline

def bfs(x ,y, target) -> int:
    global H, W, N

    if target > N:
        return 0
    
    rtn_x = -1
    rtn_y = -1
    Q = collections.deque()
    visit = [[0]*W for _ in range(H)]
    visit[x][y] = 1
    Q.append([x, y])
    while Q:
        i, j = Q.popleft()

        for d in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < H and 0 <= nj < W and not visit[ni][nj]:
                if table[ni][nj] == target: # 도착
                    visit[ni][nj] = visit[i][j] + 1
                    rtn_x = ni
                    rtn_y = nj
                    break
                
                elif table[ni][nj] < 0:
                    visit[ni][nj] = 1

                elif table[ni][nj] >= 0: # 갈 수 있음
                    visit[ni][nj] = visit[i][j] + 1
                    Q.append([ni, nj])

        if rtn_x > 0 or rtn_y > 0:
            break
    
    rtn_value = visit[rtn_x][rtn_y] - 1
    return rtn_value + bfs(rtn_x, rtn_y, target+1)

if __name__ == "__main__":
    H, W, N = map(int, input().split())
    table = []
    x, y = 0,0
    for i in range(H):
        input_lst = list(input().strip())
        change_number_lst = [0]*W
        for j in range(W):
            if input_lst[j] == '.':
                continue

            elif input_lst[j] =='S':
                x = i
                y = j
            elif input_lst[j] == 'X':
                change_number_lst[j] = -1
            else:
                change_number_lst[j] = int(input_lst[j])
        table.append(change_number_lst)

    print(bfs(x, y, 1))