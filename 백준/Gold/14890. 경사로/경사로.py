import sys
input = sys.stdin.readline

def isRoad(n: int, l:int, lst:list) -> int:
    done = [0] * n
    for i in range(1, n): # 왼쪽에서 오른쪽 이동
        if lst[i] == lst[i-1]:
            continue
        
        if abs(lst[i] - lst[i-1]) > 1: # 1 이상 차이
            return 0
        
        elif lst[i] > lst[i-1] and i-l >= 0: # 오르막
            for j in range(i-l,i):
                if done[j]:
                    return 0
                done[j] = 1

                
        elif lst[i] < lst[i-1] and i+l <= n: # 내리막
            for j in range(i,i+l):
                if done[j]:
                    return 0
                done[j] = 1
        else:
            return 0

    return 1


if __name__ == "__main__":
    N, L = map(int, input().split())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        if isRoad(N, L, Arr[i]):
            result += 1
        col = [ Arr[j][i] for j in range(N)]
        if isRoad(N, L, col):
            result += 1

    print(result)