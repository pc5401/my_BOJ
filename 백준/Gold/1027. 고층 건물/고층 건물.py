import sys
input = sys.stdin.readline


def can_i_see(n: int, num: int, bulidings: list[int]) -> int:
    rtn = 0
    inclinations = [ (bulidings[i] - bulidings[num])/(i-num)  if num != i else 0.0 for i in range(n)]

    # 왼쪽 확인
    for i in range(num):
        flag = 1
        for j in range(i + 1, num):
            if inclinations[j] <= inclinations[i]:
                flag = 0
                break 
        rtn += flag

    # 오른쪽 확인
    for i in range(num+1, n):
        flag = 1
        for j in range(num+1, i):
            if inclinations[j] >= inclinations[i]:
                flag = 0
                break 
        rtn += flag

    return rtn


def main():
    N = int(input())
    bulidings = list(map(int, input().split()))
    res = 0

    for num in range(N):
        res = max(res, can_i_see(N, num, bulidings))
    print(res)

if __name__ == "__main__":
    main()
