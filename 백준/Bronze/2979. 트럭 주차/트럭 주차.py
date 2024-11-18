import sys
input = sys.stdin.readline


def solve(cost: list[int], times: list[list[int]]):
    table = [0] * 101

    for s, e in times:
        for i in range(s, e):
            table[i] += 1

    rtn = sum([cost[t-1]*t for t in table if t])

    return rtn 
    

def main():
    # 입력값
    cost = list(map(int, input().split()))
    times = [list(map(int, input().split())) for _ in range(3)]
    # 결과 출력
    print(solve(cost, times))

        
if __name__ == '__main__':
    main()