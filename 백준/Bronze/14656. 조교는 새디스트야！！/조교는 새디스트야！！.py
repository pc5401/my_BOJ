import sys
import collections
input = sys.stdin.readline


def solve(N: int, nums: list[int]) -> int:
    rtn, i = 0, 0

    while i < N:
        num = nums[i]
        i += 1

        if num != i:
            rtn += 1

    return rtn


def main():
    # 입력
    N = int(input())
    nums = list(map(int, input().split()))
    # 풀이
    result = solve(N, nums)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
