import sys
import collections
input = sys.stdin.readline

def container_move(): # 1번
    global up_pos, down_pos, N

    up_pos = up_pos - 1 if up_pos > 0 else (2*N - 1)
    down_pos = down_pos - 1 if down_pos > 0 else (2*N -1)

    while lobot_data and lobot_data[0] == down_pos:
        lobot_data.popleft()



def lobot_move():
    global up_pos, down_pos, N

    for i, lobot in enumerate(lobot_data):
        idx = lobot+1 if 2*N > lobot+1 else 0  
        if i > 0 and lobot_data[i-1] == idx:
            continue

        if arr[idx] > 0:
            arr[idx] -= 1
            lobot_data[i] = idx
        
    while lobot_data and lobot_data[0] == down_pos:
        lobot_data.popleft()
    
    if arr[up_pos] > 0:
        arr[up_pos] -= 1
        lobot_data.append(up_pos)


if __name__ == "__main__":
    # input 값
    N, K = map(int,input().split())
    arr = list(map(int, input().split()))
    # 사용할 데이터 값
    res = 0
    up_pos, down_pos = 0, N-1
    lobot_data = collections.deque()
    while True:
        res += 1
        container_move()
        lobot_move()
        if arr.count(0) >= K:
            break

    print(res)