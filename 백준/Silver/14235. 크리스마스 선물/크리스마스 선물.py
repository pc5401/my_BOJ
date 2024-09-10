import sys
import heapq
input = sys.stdin.readline


def solve(N: int, A: list[int]) -> list[int]:
    rtn = []
    gifts = []

    for a in A:
        if a[0] == 0 and gifts:
            gift = heapq.heappop(gifts)
            rtn.append(-gift)
        elif a[0] == 0:
            rtn.append(-1)
        else:
            for new_gift in a[1:]:
                heapq.heappush(gifts, -new_gift)

    return rtn
    


def main():
    # 입력값
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    # 풀이
    result = solve(N, A)

    # 출력
    for res in result:
        print(res)


if __name__ == "__main__":
    main()

