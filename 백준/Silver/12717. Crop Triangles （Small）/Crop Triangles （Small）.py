import sys
input = sys.stdin.readline

def solve(n: int, A: int, B: int, C: int, D: int, x: int, y: int, M: int) -> int:
    cnts = [0] * 9
    X, Y = x, y
    cnts_idx = (X % 3) * 3 + (Y % 3)
    cnts[cnts_idx] += 1


    for _ in range(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        cnts_idx = (X % 3) * 3 + (Y % 3)
        cnts[cnts_idx] += 1

    mod_x = [i // 3 for i in range(9)]
    mod_y = [i % 3 for i in range(9)]

    total = 0

    for i in range(9):
        for j in range(i, 9):
            for k in range(j, 9):
                sum_x = mod_x[i] + mod_x[j] + mod_x[k]
                sum_y = mod_y[i] + mod_y[j] + mod_y[k]
                if sum_x % 3 == 0 and sum_y % 3 == 0:
                    c_i, c_j, c_k = cnts[i], cnts[j], cnts[k]
                    if i == j == k:
                        total += c_i * (c_i - 1) * (c_i - 2) // 6
                    elif i == j:
                        total += c_i * (c_i - 1) // 2 * c_k
                    elif j == k:
                        total += c_j * (c_j - 1) // 2 * c_i
                    else:
                        total += c_i * c_j * c_k
    return total

if __name__ == "__main__":
    # 입력값
    N = int(input())
    lst = [map(int, input().split()) for _ in range(N)]

    # 풀이
    result = [solve(*val) for val in lst]

    # 출력    
    for num, res in enumerate(result, start=1):
        print(f'Case #{num}: {res}')