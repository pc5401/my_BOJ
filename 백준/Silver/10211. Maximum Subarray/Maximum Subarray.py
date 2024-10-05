import sys
input = sys.stdin.readline

def solve(N: int, data: list[int]) -> int:
    sumV = data[0]
    rtn = data[0]

    for i in range(1, N):
        sumV = max(data[i], sumV + data[i])

        if sumV > rtn:
            rtn = sumV

    return rtn

if __name__ == "__main__":
    # 입력값
    T = int(input())
    nlst = []
    input_lst = []
    for _ in range(T):
        N = int(input())
        lst = list(map(int, list(input().split())))

        nlst.append(N)
        input_lst.append(lst)

    # 풀이
    result = [solve(nlst[t], input_lst[t]) for t in range(T)]

    # 출력
    for res in result:
        print(res)
