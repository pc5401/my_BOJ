import sys
input = sys.stdin.readline


def cnt_place(lst: list) -> int:
    rtn: int = 0
    cnt: int = 0
    for val in lst:
        if val:
            cnt += 1
        else:
            if cnt >= 2:
                rtn += 1
            cnt = 0
    
    if cnt >= 2:
        rtn += 1
    return rtn


def solve(N: int, room: list[list[int]]) -> tuple[int, int]:
    garo: int = 0
    sero: int = 0
    
    for i in range(N):
        garo += cnt_place(room[i])
        sero += cnt_place([room[j][i] for j in range(N)])

    return garo, sero

def main():
    # 입력값
    N: int = int(input())
    room: list = [[ 1 if i == '.' else 0 for i in input().rstrip()] for _ in range(N)]
    print(*solve(N, room))

if __name__ == "__main__":
    main()