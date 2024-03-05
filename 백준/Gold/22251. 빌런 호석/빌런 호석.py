import sys
input = sys.stdin.readline

def make_num_list(x: int, k :int) -> list:
    rtn = []

    while x:
        rtn.append(x%10)
        x //= 10

    while len(rtn) < k:
        rtn.append(0)

    return rtn

def is_possible(k: int, p: int, current_floor: list, target_floor: list) -> int:
    cnt = 0
    for i in range(k):
        cnt += display_change_table[current_floor[i]][target_floor[i]]
        
        if cnt > p:
            return 0

    return 1
    

if __name__ == '__main__':
    # 입력값
    N, K, P, X = map(int, input().split())
    res = 0
    current_floor = make_num_list(X, K)
    display_change_table = [
        [0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
        [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
        [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
        [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
        [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
        [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
        [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
        [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
        [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
        [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
    ]
    
    for n in range(1, N+1):
        if n == X:
            continue
        res += is_possible(K, P, current_floor, make_num_list(n,K))

    print(res)