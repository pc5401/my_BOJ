import sys
input = sys.stdin.readline


def solve(N: int, C: int, numbers: list[int]) -> list[int]:
    datas = dict()
    rank = 0
    for num in numbers:
        if datas.get(num):
            datas[num][0] += 1
        else:
            datas[num] = [1, rank]
            rank += 1

    result_datas = [(items[0], items[1], key) for key, items in datas.items()]
    result_datas.sort(key=lambda x : (-x[0], x[1]))

    rtn = []
    for cnt, rank, num in result_datas:
        for _ in range(cnt):
            rtn.append(num)

    return rtn


def main():
    # 입력값
    N, C = map(int, input().split())
    N: int
    C: int
    numbers: list[int] = list(map(int, input().split()))
    
    # 풀이 & 출력
    result: list[int] = solve(N, C, numbers)

    print(*result)
    
if __name__ == "__main__":
    main()

