import sys
input = sys.stdin.readline


def election_district(N: int) -> list:
    rtn = []
    for d1 in range(1, N+1):
        for d2 in range(1, N+1):
            for x in range(1, N-d1-d2+1):
                for y in range(1, N+1):
                    if y - d1 < 1:
                        continue
                    elif y + d2 > N:
                        continue
                    rtn.append([x, y, d1, d2])

    return rtn


def one_and_four(N: int, district: list) -> list:
    x, y, d1, d2 = district
    table = [[0] * (N+1) for _ in range(N+1)]

    for r in range(1, x+d1): # 1 번 구역
        for c in range(1, y+1):
            table[r][c] = 1

    for r in range(1, x+d2+1): # 2 번 구역
        for c in range(y+1, N+1):
            table[r][c] = 2
    
    for r in range(x+d1, N+1): # 3 번 구역
        for c in range(1, y-d1+d2):
            table[r][c] = 3
    
    for r in range(x+d2+1, N+1): # 4 번 구역
        for c in range(y-d1+d2, N+1):
            table[r][c] = 4

    return table

def five(table: list, district: list) -> list:
    x, y, d1, d2 = district
    Q = [district]

    while Q:
        x, y, d1, d2 = Q.pop()

        if d1 == 0 and d2 == 0:
            table[x][y] = 5
            break 
        
        elif d1 == 0:
            for d in range(d2+1):
                table[x+d][y+d] = 5
            break 
        
        elif d2 == 0:
            for d in range(d1+1):
                table[x+d][y-d] = 5
            break 
        
        for d in range(d1+1): # 1번, 4번
            table[x+d][y-d] = 5
            table[x+d2+d][y+d2-d] = 5

        for d in range(d2+1): # 2번, 3번
            table[x+d][y+d] = 5
            table[x+d1+d][y-d1+d] = 5
        
        Q.append([x+1, y, d1-1, d2-1])

    return table

def check_value(N: int, A: list, district: list):
    table = one_and_four(N, district)
    table = five(table, district)
    num_value = [0, 0, 0, 0, 0]
    for i in range(1, N+1):
        for j in range(1, N+1):
            number = table[i][j]
            people = A[i-1][j-1]
            num_value[number-1] += people
    
    minV = min(num_value)
    maxV = max(num_value)
    
    if minV == 0:
        return 1e7
    
    return maxV - minV



def solve(N: int, A: list):
    result = 1e5
    districts = election_district(N)
    for district in districts:
        value = check_value(N,A,district)
        result = min(result, value)

    return result


if __name__ == "__main__":
    # 입력 & 전처리
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(solve(N, A))