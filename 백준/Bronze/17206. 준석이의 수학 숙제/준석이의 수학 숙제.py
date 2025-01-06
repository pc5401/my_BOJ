import sys
input = sys.stdin.readline

def solve(n: int) -> int:
    rtn = [0] * (n+1)

    for i in range(1, n+1):
        if i % 7 == 0:
            rtn[i] = rtn[i-1] + i
            continue

        if i % 3 == 0:
            rtn[i] = rtn[i-1] + i
            continue

        rtn[i] = rtn[i-1]

    return rtn


if __name__ == "__main__":
    # 입력값
    T = int(input())
    lst = list(map(int, input().split()))
    
    # 풀이
    data = solve(max(lst))
    
    # 출력
    for i in lst:
        print(data[i])