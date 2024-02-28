import sys
input = sys.stdin.readline

def count_RB(v: str, s: str, rb: str):
    global N

    cnt_v= 0
    idx = rb.find(s)
    if idx == -1:
        return float('INF')
    
    for i in range(idx, N):
        if rb[i] == v:
            cnt_v += 1
    
    return cnt_v

if __name__ == '__main__':
    N = int(input())
    RB = input().rstrip()

    left_R = count_RB('R', 'B', RB)
    left_B = count_RB('B', 'R', RB)
    right_R = count_RB('R', 'B', RB[::-1])
    right_B = count_RB('B', 'R', RB[::-1])

    print(min(left_B, left_R, right_B, right_R))