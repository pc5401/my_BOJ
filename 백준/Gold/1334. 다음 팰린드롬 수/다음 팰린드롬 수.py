import sys
input = sys.stdin.readline


def solve(str_N: str) -> int:
    N = int(str_N)
    L = len(str_N)
    if N < 9:
        return N + 1
    
    if N == 9:
        return 11
    
    if L % 2 == 0: # 짝수
        n = int(str_N[0:L//2])
        val = str(n) + str(n)[::-1]
        while len(val) == L:
            if int(val) > N:
                return val
            n += 1
            val = str(n) + str(n)[::-1]
    else:
        n = str_N[0:L//2]
        for i in range(10):
            mid = str(i)
            if int(n+mid+n[::-1]) > N:
                return int(n+mid+n[::-1])

        n = int(n)
        val = str(n) + '0' + str(n)[::-1]
        while len(val) == L:
            if int(val) > N:
                return val
            n += 1
            val = str(n) + '0' + str(n)[::-1]  

    return 10**L + 1 # 자리 수 up


if __name__=="__main__":
    # 입력
    N = input().rstrip()

    # 풀이
    result = solve(N)
    
    # 출력
    print(result)