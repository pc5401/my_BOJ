import sys
input = sys.stdin.readline

def solve(n:int, lst:list) -> int:
    # 카데인 알고리즘 적용
    res = lst[0] # 최대값 저장
    sumV = lst[0] # 연속된 수익의 합을 저장

    for i in range(1,n):
        sumV = max(sumV + lst[i], lst[i])
        res = max(res, sumV)

    return res


if __name__ == "__main__":
    while True:
        N = int(input())
        if N:
            revenue = [int(input()) for i in range(N)]
            print(solve(N, revenue))
        else:
            break
            