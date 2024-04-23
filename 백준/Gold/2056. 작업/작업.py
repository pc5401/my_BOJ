import sys
input = sys.stdin.readline

def measure_time(i: int, work_data: list[int], times: list[int]) -> int:    
    longest_time = 0
    for j in work_data[1:]:
        if times[j-1] > longest_time:
            longest_time = times[j-1]

    return longest_time + work_data[0]


def solve(N: int, work_data: list[list[int]]) -> int:
    times = [0] * N
    times[0] = work_data[0][0] # 1번 작업 초기화

    for i in range(N): # DP 접근
        times[i] = measure_time(i, work_data[i], times)

    return max(times)


def main():
    # 입력값
    N: int = int(input())
    work_data: list[list[int]] = [list(map(int, input().split())) for _ in range(N)]
    # 풀이
    result: int = solve(N, work_data)
    # 출력
    print(result)


if __name__ == "__main__":
    main()