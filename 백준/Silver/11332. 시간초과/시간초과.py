import sys
input = sys.stdin.readline

def solve(S: str, N: int, T: int, L: int) -> int | str:
    if S == 'O(N)':
        return N*T <= L * 100000000
    elif S == 'O(N^2)':
        return (N**2) * T <= L * 100000000
    elif S == 'O(N^3)':
        return (N**3) * T <= L * 100000000
    elif S == 'O(2^N)':
        return (2**N) * T <= L * 100000000
    v = 1
    for i in range(1, N+1):
        if v*T > L * 100000000:
            return False
        v *= i
    
    return v*T <= L * 100000000

if __name__ == "__main__":
    # 입력값
    C = int(input())
    lst = [input().rstrip().split() for _ in range(C)]
    
    # 풀이 
    result = ['May Pass.' if solve(lst[c][0], *map(int, lst[c][1:])) else 'TLE!' for c in range(C)]
    
    # 출력
    for res in result:
        print(res)
