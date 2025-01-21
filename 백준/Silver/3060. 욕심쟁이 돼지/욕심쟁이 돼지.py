import sys
input = sys.stdin.readline


def solve(N: int, eated: list[int]) -> int:
    day = 1
    wanted = eated[:]
    M = 6
    while sum(wanted) <= N:
        day += 1
        eated = wanted[:]
        
        for i in range(M):
            wanted[i] += eated[(i+1) % M]
            wanted[i] += eated[(M+i-1) % M]
            wanted[i] += eated[(i+3) % M]
    
    return day

def main():
    # 입력
    
    result = []
    T = int(input())
    for _ in range(T):
        N = int(input())
        eated = list(map(int, input().split()))
        # 풀이
        result.append(solve(N, eated))
    

    # 출력
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
