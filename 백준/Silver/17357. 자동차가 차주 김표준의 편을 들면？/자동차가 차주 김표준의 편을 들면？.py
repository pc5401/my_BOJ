import sys
input = sys.stdin.readline


def solve(N: int, A: list[int]):
    rtn = []
    S = [0] * (N + 1)
    S2 = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i-1] + A[i-1]
        S2[i] = S2[i-1] + A[i-1] * A[i-1]


    for k in range(1, N + 1):
        max_var_num = None
        best_i = 1 
        
        for i in range(1, N - k + 2): 
            sum_ = S[i + k -1] - S[i -1]
            sum_sq = S2[i + k -1] - S2[i -1]
            
            var_num = sum_sq * k - sum_ * sum_
            
            if max_var_num is None or var_num > max_var_num:
                max_var_num = var_num
                best_i = i
        
    
        rtn.append(best_i)
    return rtn


    
def main():
    # 입력값
    N = int(input())
    A = list(map(int, input().split()))
    # 풀이
    result = solve(N, A)

    # 결과 출력
    for res in result:
        print(res)

        
if __name__ == '__main__':
    main()