import sys
input = sys.stdin.readline


def solve(N: int, A: list) -> int:
    if all( num == 0 for num in A):
        return 'ZERO'
    
    a = A
    for _ in range(1000):
        b = [abs(a[i-1] - a[i]) for i in range(1, N)]
        b.append(abs(a[N-1] - a[0]))

        if all(num == 0 for num in b):
            return 'ZERO'
        a = b

    return 'LOOP'

def main():
    # 입력값
    nlst = []
    alst = []
    T = int(input())
    for _ in range(T):
        N = int(input())    
        A = list(map(int, input().split()))
        nlst.append(N)
        alst.append(A)
    
    # 풀이
    result: list[int] = [solve(nlst[t], alst[t]) for t in range(T)]
    
    # 출력
    for res in result:
        print(res)


if __name__ == "__main__":
    main()

