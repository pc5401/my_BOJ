import sys
input = sys.stdin.readline

MOD = 1_000_000_000


def mat_mul(A: list, B: list) -> list: # 행결 연산
    return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
            [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]]

def mat_pow(mat: list, n: int) -> list:
    if n == 1:
        return mat
    elif n % 2: # 홀수
        return mat_mul(mat, mat_pow(mat, n-1))
    else: # 짝수
        half_pow = mat_pow(mat, n//2)
        return mat_mul(half_pow, half_pow)

def fibo(n: int) -> list:
    if n <= 2:
        return 1
    else:
        M = [[1, 1], [1, 0]] 
        result = mat_pow(M, n-1)
        return result[0][0] % MOD
    

if __name__ == "__main__":
    P = 1_500_000_000
    a, b = map(int, input().split())
    print((fibo(b+2) - fibo(a+1)) % MOD)