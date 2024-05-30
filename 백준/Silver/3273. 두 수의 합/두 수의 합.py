import sys
input = sys.stdin.readline


def solve(N: int, a: list[int], x: int) -> int:
    rtn = 0
    i, j = 0, N-1
    
    while i < j:
        val = a[i] + a[j]

        if val < x:
            i += 1
        
        elif val > x:
            j -= 1
        
        else:
            rtn += 1
            i += 1


    return rtn


def main():
    # 입력값
    N: int = int(input())
    a: list[int] = list(map(int, input().split()))
    x: int = int(input())
    # 풀이
    result: int = solve(N, sorted(a), x)
    # 출력
    print(result)
    
if __name__ == "__main__":
    main()
